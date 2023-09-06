#!/usr/bin/python3
"""Generates a .tgz archive and distributes the archive to the web servers"""

from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os import path

env.hosts = ['34.234.201.130', '54.236.51.83']
env.user = "ubuntu"


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


def do_deploy(archive_path):
    """Distributes the .tgz archive to the web servers"""

    if not path.isfile(archive_path):
        return False
    try:
        put(archive_path, "/tmp/")

        directory_path = archive_path.split(".")[0]
        directory_path = directory_path.split("/")[-1]
        archive_path = archive_path.split("/")[-1]

        sudo("mkdir -p /data/web_static/releases/{}/".format(directory_path))

        full_path = "/data/web_static/releases/{}".format(directory_path)

        sudo("tar -xvzf /tmp/{} -C {}".format(archive_path, full_path))
        sudo("rm -rf /tmp/{}".format(archive_path))
        sudo("mv -f {}/web_static/* {}".format(full_path, full_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -sf {} /data/web_static/current".format(full_path))

        return True
    except Exception:
        return False
