import click
from omicsdi_client import OmcicsClient, url_path_join
import os
from urllib.parse import urlsplit
import shutil
import sys

client = OmcicsClient()


def make_dir(output, acc_number):

    if output:
        dir_path = url_path_join(output, acc_number)
    else:
        dir_path = acc_number

    if os.path.exists(dir_path):
        shutil.rmtree(dir_path)

    os.makedirs(dir_path)

    return dir_path


def source_from_id(acc):
    api_output = client.get_source(acc)
    if api_output['datasets']:
        if len(api_output['datasets']) > 1:
            hits = []
            for dataset in api_output['datasets']:
                if dataset['id'] == acc:
                    hits.append(dataset)

            if len(hits) == 1:
                source = hits[0]['source']
                return source
            else:
                click.echo('INFO')
                click.echo(f'{acc} is not a unique ID, leading to multiple hits.')
                sys.exit()
        else:
            source = api_output['datasets'][0]['source']
            return source
    else:
        click.echo('INFO')
        click.echo(f'{acc} could not be found in one of the repositories.')
        sys.exit()


def file_links(source, acc):
    api_output = client.get_data(source, acc)
    file_links = []
    if api_output['file_versions']:
        files = api_output['file_versions'][0]['files']
        for ext, files in files.items():
            for url in files:
                file_links.append(url)

    else:
        click.echo('INFO')
        click.echo(f'The accession {acc} is found in the {source} database, but contains no files.')
        sys.exit()

    return file_links


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


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo('Version 0.1')
    ctx.exit()


@click.command(context_settings={'help_option_names': ['-h', '--help']})
@click.option('--version', '-v',  callback=print_version, expose_value=False, is_eager=True, is_flag=True, help="Print version number")
@click.argument('acc_number')
@click.option(
    '--download', '-d',  is_flag=True,
    help='Use this flag to download the files in the current directory or a specified output directory',
)
@click.option(
    '--output', '-o',  default=None,  type=click.Path(exists=True),
    help='Output directory when downloading files (default: CWD)',
)
def main(acc_number, download, output):
    """
\b                                                     
   ___        _       ___  _    __     _      _            
  / _ \ _ __ (_)__ __|   \(_)  / _|___| |_ __| |_  ___ _ _ 
 | (_) | '  \| / _(_-< |) | | |  _/ -_)  _/ _| ' \/ -_) '_|
  \___/|_|_|_|_\__/__/___/|_| |_| \___|\__\__|_||_\___|_|                                                                                            
\b                                                   
    Command Line Interface to fetch data from OmicsDi.
    """

    source = source_from_id(acc_number)
    file_urls = file_links(source, acc_number)

    # Download section
    if download and file_urls:
        dir_path = make_dir(output, acc_number)
        for file_url in file_urls:
            info = url_info(file_url)
            click.echo("Downloading...  " + filename_process(info['filename']))
            if info['scheme'] == 'ftp':
                client.download_ftp_files(
                    info['domain'], info['project_dir'], dir_path, info['filename'])
            elif info['scheme'] == 'https' or info['scheme'] == 'http':
                info = url_info(file_url)
                client.download_http_files(
                    file_url, filename_process(info['filename']), dir_path)
            else:
                click.echo('--> Scheme is not supported for ' + file_url)
    # DEFAULT: Printing URLS when -d is not given
    else:
        pretty = '\n'.join(file_urls)
        click.echo(pretty)


if __name__ == "__main__":
    main()
