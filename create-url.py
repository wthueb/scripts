#!/usr/bin/env python

import argparse
import os


parser = argparse.ArgumentParser(description='creates shortcut to link')

parser.add_argument('filename', help='the name of the file for the shortcut with no extension')

parser.add_argument('url', help='the url to link to')

args = parser.parse_args()

with open(args.filename + '.url', 'w') as f:
    f.write('[InternetShortcut]\n')
    f.write('URL=' + args.url + '\n')
    f.write('IconIndex=0')

print(args.filename + '.url has been created, pointing to ' + args.url)
print('path: ' + os.path.join(os.getcwd(), args.filename + '.url'))
