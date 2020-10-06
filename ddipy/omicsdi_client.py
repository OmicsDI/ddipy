import json
import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
import urllib.request
import ftplib
import time
import re
import os
import shutil
import click
import sys


def url_path_join(*args):
    """Join path(s) in URL using slashes"""

    return '/'.join(s.strip('/') for s in args)


class OmcicsClient:
    def __init__(self):
        self.endpoint = 'https://www.omicsdi.org:443/'

    def get_source(self, acc_numb):
        """"Get source from Id"""

        return self.fetch_object(f'/ws/dataset//search?query={acc_numb}&sortfield=id')

    def get_data(self, source, acc_numb):
        """"Get ftp links from Id"""

        return self.fetch_object(f'/ws/dataset/{source}/{acc_numb}')

    def fetch_object(self, path):
        """API object fetcher"""

        url = url_path_join(self.endpoint, path)
        session = requests.Session()
        retry = Retry(connect=3, backoff_factor=15)
        adapter = HTTPAdapter(max_retries=retry)
        session.mount('http://', adapter)
        session.mount('https://', adapter)
        r = session.get(url)

        if r.status_code != requests.codes.ok:
            click.echo("problem with request: " + str(r))
            raise RuntimeError("Non-200 status code")
        
        else:
            return r.json()

    def download_ftp_files(self, domain, project_dir, dir_path, filename):
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
                click.echo('--> Please check if ' + filename +
                      ' exists in ' + project_dir + ' on the domain ' + domain)

    def download_http_files(self, file_url, filename, dir_path):
        """Download http files in given directory"""

        file_path = url_path_join(dir_path, filename)
        try:
            session = requests.Session()
            retry = Retry(connect=3, backoff_factor=15)
            adapter = HTTPAdapter(max_retries=retry)
            session.mount('http://', adapter)
            session.mount('https://', adapter)
            r = session.get(file_url)

            if r.status_code != requests.codes.ok:
                click.echo('--> ERROR Response ' + str(r.status_code) + ', reason: ' + str(r.reason))
                click.echo('--> Please check if ' + file_url + ' is reachable')

            else:
                with urllib.request.urlopen(file_url) as response, open(file_path, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)

        except urllib.request.HTTPError as e:
            click.echo('-->', e)
            click.echo('--> Please check if ' + file_url + ' is reachable')