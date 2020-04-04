#!/usr/bin/env python

from subprocess import run

res = run('pip freeze'.split(), capture_output=True)

packages = [s.strip() for s in res.stdout.decode('utf-8').split('\n') if s.strip()]
packages = [p.split('==')[0] for p in packages]

packages_str = ' '.join(packages)

command = f'pip install --upgrade {packages_str}'

print(command, flush=True)

run(command.split())
