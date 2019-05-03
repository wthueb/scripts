#!/usr/bin/env python3

import argparse
import sys

import requests

from secrets import PASTEBIN_DEV_KEY, PASTEBIN_USER_KEY

class Parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)

        self.print_help()

        sys.exit(1)

parser = Parser(description='uploads file to pastebin')

parser.add_argument('file',
                    help='the file to upload. default: stdin',
                    nargs='?', default=sys.stdin)

args = parser.parse_args()

if isinstance(args.file, str):
    with open(args.file) as f:
        text = f.read()
else:
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
        'api_paste_private': '0', # 0:public 1:unlisted 2:private
        'api_paste_expire_date': 'N' # never expire
        }

r = requests.post(url, data=data)

print(r.text)
