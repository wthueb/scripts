#!/usr/bin/env python3

import os
import sys

if len(sys.argv) != 3:
    print('usage: ./create-url.py filename url')

    exit(0)

filename = sys.argv[1]
url = sys.argv[2]

with open(filename + '.url', 'w') as f:
    f.write('[InternetShortcut]\n')
    f.write('URL=' + url + '\n')
    f.write('IconIndex=0')

print(filename + '.url has been created, pointing to ' + url)
print('path: ' + os.path.join(os.getcwd(), filename + '.url'))
