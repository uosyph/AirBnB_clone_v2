#!/usr/bin/python3
"""Cleans outdated archives"""

from fabric.api import *
from os import listdir


def do_clean(number=0):
    """Cleans outdated archives"""

    number = 1 if int(number) == 0 else int(number)
    archives = sorted(listdir("versions"))
    [archives.pop() for _ in range(number)]

    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for _ in range(number)]
        [run("rm -rf ./{}".format(a)) for a in archives]
