#!/usr/bin/env python3

import argparse
import sys

from pushover import Client


class Parser(argparse.ArgumentParser):
    def error(self, message):
        sys.stderr.write('error: %s\n' % message)

        self.print_help()

        sys.exit(1)


parser = Parser(description=f'sends notification to pushover')

parser.add_argument('--title', help='the title of the push')
parser.add_argument('--attachment', help='an image file to be attached')
parser.add_argument('text', help='the text to push. default: stdin', nargs='?', default=sys.stdin)

args = parser.parse_args()

# relies on ~/.pushoverrc to get api token and user key
client = Client()

client.send_message(args.text, title=args.title, attachment=args.attachment)
