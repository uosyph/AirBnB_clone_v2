#!/usr/bin/python3
"""Generates a .tgz archive and distributes the archive to the web servers"""

from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os import path

env.hosts = ['34.234.201.130', '54.236.51.83']


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


def do_deploy(archive_path):
    """Distributes the .tgz archive to the web servers"""

    if not path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")

        directory_path = archive_path.split(".")[0]
        directory_path = directory_path.split("/")[-1]
        archive_path = archive_path.split("/")[-1]

        sudo(f"mkdir -p /data/web_static/releases/{directory_path}/")

        full_path = f"/data/web_static/releases/{directory_path}"

        sudo(f"tar -xvzf /tmp/{archive_path} -C {full_path}")
        sudo(f"rm -rf /tmp/{archive_path}")
        sudo(f"mv -f {full_path}/web_static/* {full_path}")
        sudo("rm -rf /data/web_static/current")
        sudo(f"ln -sf {full_path} /data/web_static/current")

        return True
    except Exception:
        return False
