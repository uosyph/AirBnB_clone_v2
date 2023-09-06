#!/usr/bin/python3
"""Automating archiveing and distributes the archive to the web servers"""

from fabric.api import local, run, env, put, sudo
from datetime import datetime
from os import path
from io import StringIO

env.hosts = ['34.234.201.130', '54.236.51.83']


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


def deploy():
    """Automate archiveing and deployment"""

    if not do_pack():
        return False
    return do_deploy(f"versions/{do_pack()}")


def do_clean(number=0):
    """Cleans old versions from the directory"""

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
        local(f"rm -rf versions/{versions[i]}")

    code = "ls -ltr /data/web_static/releases | rev | cut -d ' ' -f1 | rev"
    fk_value = sudo(code, stdout=file_handler)

    file_handler.seek(0)
    fk_names = []
    for line in file_handler.readlines():
        data = line.split()[-1]
        if data.startswith("web_static"):
            fk_names.append(data)

    for i in range(len(fk_names) - number):
        sudo(f"rm -rf /data/web_static/releases/{fk_names[i]}")
