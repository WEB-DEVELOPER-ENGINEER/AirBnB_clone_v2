#!/usr/bin/python3
""" Fabfile to generates a .tgz archive from the contents of web_static """
from datetime import datetime
from fabric.api import local


def do_pack():
    '''
        generates a .tgz archive from the contents of the web_static folder
    '''
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("tar -vzfc {} web_static/".format(filename))
    if result.succeeded:
        return (filename)
    else:
        return None
