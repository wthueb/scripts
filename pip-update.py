#!/usr/bin/env python3

import pkg_resources
from subprocess import call

packages = []

for dist in pkg_resources.working_set:
    if not dist.project_name.startswith('-'):
        packages.append(dist.project_name)

call('pip install --upgrade ' + ' '.join(packages), shell=True)
