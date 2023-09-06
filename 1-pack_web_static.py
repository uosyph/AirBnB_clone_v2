#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static directory"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the web_static directory"""

    local("mkdir -p versions")
    try:
        time = datetime.now().strftime('%Y%m%d%H%M%S')
        file_name = "web_static_{}.tgz".format(time)
        local("tar -cvzf versions/{} web_static".format(file_name))
        return file_name
    except Exception:
        return
