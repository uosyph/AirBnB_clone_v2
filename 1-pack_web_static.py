#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static directory"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the web_static directory"""

    local("mkdir -p versions")
    now = datetime.today()
    try:
        file_name = "web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                         now.month,
                                                         now.day,
                                                         now.hour,
                                                         now.minute,
                                                         now.second)
        local(f"tar -cvzf versions/{file_name} web_static")
        return file_name
    except Exception:
        return
