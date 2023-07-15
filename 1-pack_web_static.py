#!/usr/bin/python3
"""Generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone"""

from datetime import datetime
from fabric.api import local


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder
    """
    now = datetime.now()
    file_name = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year, now.month, now.day, now.hour, now.minute, now.second)
    local("mkdir -p versions")
    result = local("tar -czvf {} -C web_static .".format(file_name))
    if result.succeeded:
        return file_name
    else:
        return None
