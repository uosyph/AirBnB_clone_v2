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
    now = datetime.today()
    try:
        file_name = f"web_static_{datetime.now().strftime('%Y%m%d%H%M%S')}.tgz"
        local(f"tar -cvzf versions/{file_name} web_static")
        return file_name
    except Exception:
        return


def do_deploy(archive_path):
    """Distributes the .tgz archive to the web servers"""

    if not path.isfile(archive_path):
        return False
    try:
        results = []
        result = put(archive_path, "/tmp")
        results.append(result.succeeded)

        archive = path.archive(archive_path)
        if archive[-4:] == ".tgz":
            directory_path = archive[:-4]

        full_path = f"/data/web_static/releases/{directory_path}"

        run(f"mkdir -p {full_path}")
        run(f"tar -xzf /tmp/{archive} -C {full_path}")
        run(f"rm /tmp/{archive}")
        run(f"mv {full_path}/web_static/* {full_path}")
        run(f"rm -rf {full_path}/web_static")
        run("rm -rf /data/web_static/current")
        run(f"ln -s {full_path} /data/web_static/current")

        return True
    except Exception:
        return False
