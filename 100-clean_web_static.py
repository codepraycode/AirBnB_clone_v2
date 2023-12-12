#!/usr/bin/python3
"""Script to deploy"""
import time
from fabric.api import *
import os

env.hosts = ["54.82.210.126", "18.233.67.22"]
env.user = "ubuntu"


def do_clean(number=0):
    """
        Clean deployment
    """

    number = int(number)

    if number == 0:
        number = 2
    else:
        number += 1

    local("cd versions; ls -t | tail -n +{} | xargs rm -rf".format(number))
    path = "/data/web_static/releases"
    run("cd {}; ls -t | tail -n +{} | xargs rm -rf".format(path, number))
