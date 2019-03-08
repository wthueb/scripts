#!/usr/bin/env python3

import argparse
import sys

import requests

from secrets import PASTEBIN_DEV_KEY, PASTEBIN_USER_KEY

parser = argparse.ArgumentParser(description='uploads file to pastebin')

parser.add_argument('file',
                    help='the file to upload. reads from stdin if file is not specified',
                    nargs='?', default=sys.stdin)

args = parser.parse_args()

if isinstance(args.file, str):
    with open(args.file) as f:
        text = f.read()
else:
    text = args.file.read()

url = 'https://pastebin.com/api/api_post.php'

data = {
        'api_dev_key': PASTEBIN_DEV_KEY,
        'api_user_key': PASTEBIN_USER_KEY,
        'api_paste_name': args.file, # title
        'api_option': 'paste',
        'api_paste_code': text,
        'api_paste_private': '1', # 0:public 1:unlisted 2:private
        'api_paste_expire_date': 'N' # never expire
        }

r = requests.post(url, data=data)

print(r.text)
