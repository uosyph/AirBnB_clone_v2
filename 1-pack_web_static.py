#!/usr/bin/python3
"""Generates a .tgz archive from the contents of the web_static directory"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Generates a .tgz archive from the web_static directory"""

    local("mkdir -p versions")
    try:
        file_name = f"web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
        local(f"tar -cvzf versions/{file_name} web_static")
        return file_name
    except Exception:
        return
