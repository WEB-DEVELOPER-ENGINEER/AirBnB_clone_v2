#!/usr/bin/python3
"""deletes out-of-date archives"""
import os
from fabric.api import *

env.hosts = ["34.207.253.78", "3.84.239.44"]


def do_clean(number=0):
    """Delete out-of-date archives.
    Args:
        number (int): If number is 0 or 1, keeps only the most recent archive.
        If number is 2, keeps the most and second-most recent archives, etc.
    """
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    archives = archives[:-number]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        archives = archives[:-number]
        [run("rm -rf ./{}".format(a)) for a in archives]
