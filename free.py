#!/usr/bin/env python3

import subprocess
import re

ps = subprocess.Popen(['ps', '-caxm', '-orss,comm'], stdout=subprocess.PIPE).communicate()[0].decode()
vm = subprocess.Popen(['vm_stat'], stdout=subprocess.PIPE).communicate()[0].decode()

ps_lines = ps.split('\n')

sep = re.compile('[\s]+')

rss_total = 0 # kB

for row in range(1, len(ps_lines)):
    row_text = ps_lines[row].strip()

    row_elems = sep.split(row_text)

    try:
        rss = float(row_elems[0]) * 1024
    except:
        rss = 0

    rss_total += rss

vm_lines = vm.split('\n')

sep = re.compile(':[\s]+')

vm_stats = {}

for row in range(1, len(vm_lines) - 2):
    row_text = vm_lines[row].strip()

    row_elems = sep.split(row_text)

    vm_stats[row_elems[0]] = int(row_elems[1].strip('\.')) * 4096

print('wired memory:\t\t%d MB' % (vm_stats['Pages wired down'] / 1024 / 1024))
print('active memory:\t\t%d MB' % (vm_stats['Pages active'] / 1024 / 1024))
print('inactive memory:\t%d MB' % (vm_stats['Pages inactive'] / 1024 / 1024))
print('real mem total (ps):\t%.3f MB' % (rss_total / 1024 / 1024))
print('free memory:\t\t%d MB' % (vm_stats['Pages free'] / 1024 / 1024))
