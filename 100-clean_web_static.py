#!/usr/bin/python3
"""Cleans outdated archives"""

from fabric.api import local, sudo
from io import StringIO


def do_clean(number=0):
    """Cleans outdated archives"""

    file_handler = StringIO()
    versions = []
    number = int(number)

    if number == 0:
        number = 1

    reverse_ls = "ls -ltr versions | rev | cut -d ' ' -f1 | rev"

    value = local(reverse_ls, capture=True)
    for line in value.splitlines():
        versions.append(line)

    versions.pop(0)
    for i in range(len(versions) - number):
        local("rm -rf versions/{}".format(versions[i]))

    code = "ls -ltr /data/web_static/releases | rev | cut -d ' ' -f1 | rev"
    fk_value = sudo(code, stdout=file_handler)

    file_handler.seek(0)
    fk_names = []
    for line in file_handler.readlines():
        data = line.split()[-1]
        if data.startswith("web_static"):
            fk_names.append(data)

    for i in range(len(fk_names) - number):
        sudo("rm -rf /data/web_static/releases/{}".format(fk_names[i]))
