#!/usr/bin/python3
"""Generate a .tgz archive from web_static folder"""
from fabric.api import local
import time


def do_pack():
    """
        Generate a tgz archive from web_static folder
    """

    try:
        _dir = "versions/web_static_{}.tgz".format(
            time.strftime("Y%m%d%H%M%S")
        )

        local("mkdir -p versions")
        local("tar -cvzf {} web_static/".format(_dir))

        return _dir
    except Exception as e:
        return None
