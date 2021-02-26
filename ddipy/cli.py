import click
import os
from urllib.parse import urlsplit
import json
import requests
from urllib3.util.retry import Retry
import urllib.request
import ftplib
import re
import shutil
import click
import sys
from ddipy.dataset_client import DatasetClient
from ddipy._version import __version__
import hashlib


def url_path_join(*args):
    """Join path(s) in URL using slashes"""

    return '/'.join(s.strip('/') for s in args)


def source_from_id(acc):
    client = DatasetClient()
    api_output = client.search(acc, "id")
    if api_output.datasets:
        datasets = api_output.datasets
        if len(datasets) > 1:
            hits = []
            for dataset in datasets:
                if dataset.accession == acc:
                    hits.append(dataset)

            if len(hits) == 1:
                source = hits[0].database
                return source
            else:
                click.echo('INFO')
                click.echo(
                    f'{acc} is not a unique ID, leading to multiple hits.')
                sys.exit()
        else:
            source = datasets[0].database
            return source
    else:
        click.echo('INFO')
        click.echo(f'{acc} could not be found in one of the repositories.')
        sys.exit()


def file_links(source, acc):
    client = DatasetClient()
    api_output = client.get_dataset_details(source, acc)
    file_links = {}
    if api_output.files:
        files = api_output.files[0]['files']

    else:
        click.echo('INFO')
        click.echo(
            f'The accession {acc} is found in the {source} database, but contains no files.')
        sys.exit()

    return files


def url_info(url):
    if not '://' in url:
        if url.startswith('ftp.'):
            url = 'ftp://' + url
        else:
            url = 'https://' + url
    url = url.strip('/')
    split_url = urlsplit(url)
    project_dir = "".join(split_url.path.rpartition("/")[:-1])
    domain = split_url.hostname
    scheme = split_url.scheme
    filename = url.split('/')[-1]

    return {'project_dir': project_dir, 'domain': domain, 'scheme': scheme, 'filename': filename}


def filename_process(filename):
    if 'filename=' in filename:
        return filename.split('filename=')[1]
    else:
        return filename


def download_ftp_files(domain, project_dir, dir_path, filename):
    """Download ftp files in given directory"""

    with ftplib.FTP(domain) as ftp:
        try:
            ftp.login()
            ftp.cwd(project_dir)
            file_path = url_path_join(dir_path, filename)
            localfile = open(file_path, 'wb')
            ftp.retrbinary(
                "RETR " + filename, localfile.write)
            localfile.close()

        except ftplib.all_errors as e:
            click.echo('--> FTP error:', e)
            click.echo(
                f'--> Please check if {filename} exists in {project_dir} on the domain {domain}')


def download_http_files(file_url, filename, dir_path):
    """Download http files in given directory"""

    file_path = url_path_join(dir_path, filename)
    try:
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=15)
        adapter = requests.adapters.HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        r = session.get(file_url)

        if r.status_code != requests.codes.ok:
            click.echo(
                f'--> ERROR Response {r.status_code} reason: {r.reason}')
            click.echo(f'--> Please check if {file_url} is reachable')

        else:
            with urllib.request.urlopen(file_url) as response, open(file_path, 'wb') as out_file:
                shutil.copyfileobj(response, out_file)

    except urllib.request.HTTPError as e:
        click.echo('-->', e)
        click.echo(f'--> Please check if {file_url} is reachable')


def download_hub(info, file_url, output):
    click.echo(f"Downloading...  {filename_process(info['filename'])}")
    if info['scheme'] == 'ftp':
        download_ftp_files(
            info['domain'], info['project_dir'], output, info['filename'])
    elif info['scheme'] == 'https' or info['scheme'] == 'http':
        info = url_info(file_url)
        download_http_files(
            file_url, filename_process(info['filename']), output)
    else:
        click.echo(f'--> Scheme is not supported for {file_url}')


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(__version__)
@click.argument('acc_number')
@click.option(
    '--download', '-d',  is_flag=True,
    help='Use this flag to download the files in the current directory or a specified output directory',
)
@click.option(
    '--verbose', '-v',  is_flag=True,
    help='Use this flag to display th extensions',
)
@click.option(
    '--output', '-o',  default=".",  type=click.Path(exists=True),
    help='Output directory when downloading files (default: CWD)',
)
@click.option(
    '--input', '-i',
    help='Output directory when downloading files (default: CWD)',
)
def main(acc_number, download, output, verbose, input):
    """                                            
    Command Line Interface to fetch data from OmicsDi.
    """

    source = source_from_id(acc_number)
    file_urls = file_links(source, acc_number)

    # Download section
    if download and file_urls:
        for ext, url_group in file_urls.items():
            for file_url in url_group:
                checksum = hashlib.md5(file_url.encode()).hexdigest()
                info = url_info(file_url)
                #check if identifiers are given for selection
                if input:
                    if checksum[:10] in re.split(', |,', input.strip()):
                        download_hub(info, file_url, output)
                else:
                    download_hub(info, file_url, output)

    # DEFAULT: Printing URLS when -d is not given
    else:
        for ext, url_group in file_urls.items():
            for file_url in url_group:
                if verbose:
                    # checksum as unique identifier within accessionnumber allowing selection
                    url_id = hashlib.md5(file_url.encode()).hexdigest()
                    info = url_info(file_url)
                    click.echo(f"{url_id[:10]}\t{ext}\t{filename_process(info['filename'])}\t{file_url}")
                else:
                    click.echo(file_url)


if __name__ == "__main__":
    main(sys.argv[1:])
