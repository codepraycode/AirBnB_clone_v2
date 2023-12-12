#!/usr/bin/python3
"""Script to distribute archive to web servers
"""

from datetime import datetime
from fabric.api import *
import os

env.hosts = ["54.82.210.126", "18.233.67.22"]
env.user = "ubuntu"


def do_pack():
    """
        Generate a tgz archive from web_static folder
    """

    date = time.strftime("Y%m%d%H%M%S")
    
    local("mkdir -p versions")

    archieved_path = "versions/web_static_{}.tgz".format(date)
    zipped_archive = local("tar -cvzf {} web_static".format(archieved_path))

    if zipped_archive.succeeded:
        return archieved_path
    else:
        return None


def do_deploy(archive_path):
    """Distribute archive to servers

    Args:
        archive_path (string): Path to the generated archive
    """

    if not os.path.exists(archive_path):
        return False
    

    archive_file = archive_path[9:]
    newest_version = "data/web_static/releases/" + archive_file[:-4]
    archive_file = "/tmp/" + archive_file
    put(archive_path, "/tmp/")
    run("sudo mkdir -p {}".format(newest_version))
    run("sudo tar -xzf {} -C {}/".format(archive_file, newest_version))
    run("sudo rm {}".format(archive_file))
    run("sudo mv {}/web_static/* {}".format(newest_version, newest_version))
    run("sudo rm -rf {}/web_static".format(newest_version))
    run("sudo rm -rf /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(newest_version))

    print("New version deployed!")
    return True
