#!/usr/bin/python3
""" Fabfile to generates a .tgz archive from the contents of web_static """
from datetime import datetime
from fabric.api import local


def do_pack():
    """create .tgz archive from the contents of the web_static folder"""
    local("mkdir -p versions")
    now = datetime.now()
    filename = "versions/web_static_{}{}{}{}{}{}.tgz".format(now.year,
                                                             now.month,
                                                             now.day,
                                                             now.hour,
                                                             now.minute,
                                                             now.second)
    result = local("tar -vczf {} web_static".format(filename))
    if result.succeeded:
        return (filename)
    else:
        return None


archive_path = do_pack()
