#!/usr/bin/python3
"""create .tgz archive from the contents of
the web_static folder of your AirBnB Clone"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """Compress web_static folder"""
    d = datetime.now()
    local("mkdir -p versions")
    file_name = 'versions/web_static_{}{}{}{}{}{}.tgz\
'.format(d.year, d.month, d.day, d.hour, d.minute, d.second)
    status = local("tar -cvzf" + file_name + " ./web_static/", capture=True)
    if status.succeeded:
        return file_name
    return None
