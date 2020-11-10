#!/usr/bin/env python3

import argparse
import re
import sys

from termcolor import colored


class Parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)

        self.print_help()

        sys.exit(1)


parser = Parser(description='grep, but using perl compatible regular expressions')

parser.add_argument('-o', '--only-match',
                    help='only print the matching part of the line',
                    dest='only_match',
                    action='store_true')

parser.add_argument('pattern', help='the pattern to search for')

parser.add_argument('file',
                    help='the file to search for the pattern. default: stdin',
                    nargs='?',
                    type=argparse.FileType('r'),
                    default=sys.stdin)

args = parser.parse_args()

pattern = re.compile(args.pattern)

for line in args.file.readlines():
    line = line.strip()

    match = pattern.search(line)

    if match:
        if args.only_match:
            print(colored(match.group(), 'green'))
        else:
            start_of_group = match.span()[0]
            end_of_group = match.span()[1]

            output = line[:start_of_group] + colored(match.group(), 'green') + line[end_of_group:]

            print(output)
