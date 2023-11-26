#!/usr/bin/env python3

import pysftp
import sys
from pathlib import Path
from io import BytesIO
import re

LOCAL_DIR = 'C:\\My\\Directory\\' # with closing separator
REMOTE_DIR = '/home/directory/' # absolute directory with closing separator


class Sftp:
    def __init__(self, host, port, username, password, deploymentDirectory, verbose=True):
        if deploymentDirectory[-1] != '/': deploymentDirectory += '/'
        self.deployment_directory = deploymentDirectory
        self.verbose = verbose
        self.connection = None
        try:
            self.connection = pysftp.Connection(host, port=port, username=username, password=password)
        except Exception:
            print('Could not connect to remote sftp server with the specified arguments.', file=sys.stderr)
            sys.exit(1)

    def __del__(self):
        self.close()

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None

    def read_text_file(self, remote_file_name):
        full_remote_file_name = self.deployment_directory + remote_file_name
        b = BytesIO()
        self.connection.getfo(full_remote_file_name, b)
        s = b.getvalue().decode('utf-8')
        return s


    def remote_file_exists(self, remote_file_name):
        full_remote_file_name = self.deployment_directory + remote_file_name
        return self.connection.isfile(full_remote_file_name)


def compare(local_text, remote_text):
    """
    The files could be the same except for the way the hosts handle the line-termination sequence (Windows: \r\n, Unix/Linux: \n, Mac: \r).
    So, let's normalize:
    """
    rex = re.compile(r'\r\n?')
    local_text = rex.sub('\n', local_text)
    remote_text = rex.sub('\n', remote_text)
    return local_text == local_text


def main():
    sftp = Sftp(host='demo.com', port=22, username='xxxx', password='xxxx', deploymentDirectory=REMOTE_DIR)
    l_local_dir = len(LOCAL_DIR)
    for path in Path(LOCAL_DIR).rglob('*.csv'):
        dir, file_name = path.parent, path.name
        # compute relative remote path:
        remote_file_name = str(dir)[l_local_dir:].replace('\\', '/') + '/' + file_name
        if not sftp.remote_file_exists(remote_file_name):
            print(f'{path}: This file does not exist in remote directory.')
        else:
            remote_text = sftp.read_text_file(remote_file_name)
            with path.open(encoding='utf-8') as f:
                local_text = f.read()
                if compare(local_text, remote_text):
                    print(f'{path} exits in the remote directory and matches.')
                else:
                    print(f'{path} exits in the remote directory but does not match.')
    sftp.close()


main()
