#!/usr/bin/env python

import argparse
import sys

import requests

try:
    from config import HASTEBIN_BASE_URL
except:
    HASTEBIN_BASE_URL = 'https://hastebin.com'


class Parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)

        self.print_help()

        sys.exit(1)


parser = Parser(description=f'uploads file to {HASTEBIN_BASE_URL}')

parser.add_argument('file', help='the file to upload. default: stdin', nargs='?',
        default=sys.stdin)

args = parser.parse_args()

if isinstance(args.file, str): # reading from a file
    with open(args.file) as f:
        text = f.read()
else: # reading from stdin
    try:
        text = args.file.read()
    except KeyboardInterrupt:
        parser.print_help()

        sys.exit(130)

url = f'{HASTEBIN_BASE_URL}/documents'

r = requests.post(url, data=text)

if r.status_code == 200:
    key = r.json()['key']
    url = f'{HASTEBIN_BASE_URL}/{key}'

    print(url)
else:
    print(f'there was an error uploading to {HASTEBIN_BASE_URL}')
