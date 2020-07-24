#!/usr/bin/env python3

import argparse
import base64
import sys

import requests

from config import IMGUR_CLIENT_ID


class Parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write(f'error: {message}\n')

        self.print_help()

        sys.exit(1)


parser = Parser(description='uploads image file to imgur.com')

parser.add_argument('file', help='the image file to upload. default: stdin')

args = parser.parse_args()

with open(args.file, 'rb') as f:
    image = base64.b64encode(f.read())

headers = {'Authorization': f'Client-ID {IMGUR_CLIENT_ID}'}

data = {'image': image, 'type': 'base64'}

r = requests.post('https://api.imgur.com/3/image', headers=headers, data=data)

if r.status_code < 200 or r.status_code > 299:
    sys.stderr.write('error: imgur returned status code {r.status_code}')

    sys.exit(1)

print(r.json()['data']['link'])
