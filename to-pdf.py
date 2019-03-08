#!/usr/bin/env python3

from os.path import basename, isfile
import re
from sys import argv

import convertapi

from secrets import CONVERTAPI_KEY

usage = 'usage: to-pdf INPUT_FILE [OUTPUT_FILE]'

convertapi.api_secret = CONVERTAPI_KEY

if len(argv) < 2 or len(argv) > 3:
    print(usage)
    exit(1)

input_file = argv[1]

if not isfile(input_file):
    print(argv[1] + ' is not a valid file')
    print(usage)
    exit(1)

if len(argv) == 3:
    output_file = argv[2]
else:
    output_file = basename(input_file)

    output_file = re.match(r'.*(?=\.)', output_file).group()

    output_file += '.pdf'

result = convertapi.convert('pdf', { 'File': input_file })

result.file.save(output_file)

print(input_file + ' -> ' + output_file) 
