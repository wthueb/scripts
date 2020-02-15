#!/usr/bin/env python

import argparse
import sys

import requests

from config import PASTEBIN_DEV_KEY

try:
    from config import PASTEBIN_USER_KEY
except:
    PASTEBIN_USER_KEY = ''


class Parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)

        self.print_help()

        sys.exit(1)


parser = Parser(description='uploads file to pastebin')

parser.add_argument('file', help='the file to upload. default: stdin', nargs='?',
        default=sys.stdin)

parser.add_argument('-u', '--unlisted', action='store_true',
        help='share as unlisted (10 paste maximum for free accounts)')

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

url = 'https://pastebin.com/api/api_post.php'

data = {
        'api_dev_key': PASTEBIN_DEV_KEY,
        'api_user_key': PASTEBIN_USER_KEY,
        'api_paste_name': args.file, # title
        'api_option': 'paste',
        'api_paste_code': text,
        'api_paste_private': f'{int(args.unlisted)}', # 0:public 1:unlisted 2:private
        'api_paste_expire_date': 'N' # never expire
}

r = requests.post(url, data=data)

if r.status_code == 200:
    print(r.text)
else:
    print(f'there was an error: {r.text}')
