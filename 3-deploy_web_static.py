#!/usr/bin/python3
"""Generates a .tgz archive from web_static directory and distributes it"""
from datetime import datetime
from fabric.api import local
import os.path
from fabric.api import env
from fabric.api import put
from fabric.api import sudo

env.hosts = ["34.207.253.78", "3.84.239.44"]


def do_pack():
    '''
        generates a .tgz archive from the contents of the web_static folder
    '''
    local("mkdir -p versions")
    date = datetime.now().strftime("%Y%m%d%H%M%S")
    filename = "versions/web_static_{}.tgz".format(date)
    result = local("tar -cvzf {} web_static/".format(filename))
    if result.succeeded:
        return (filename)
    else:
        return None


def do_deploy(archive_path):
    """
    Args:
        archive_path (str): The path of the archive to distribute.
    Return:
        If the file doesn't exist at archive_path or an error occurs - False.
        Otherwise - True.
    """
    if os.path.isfile(archive_path) is False:
        return False
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if sudo("mkdir -p /data/web_static/releases/{}/".
            format(name)).failed is True:
        return False
    if sudo("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".
            format(file, name)).failed is True:
        return False
    if sudo("rm /tmp/{}".format(file)).failed is True:
        return False
    if sudo("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/releases/{}/web_static".
            format(name)).failed is True:
        return False
    if sudo("rm -rf /data/web_static/current").failed is True:
        return False
    if sudo("ln -s /data/web_static/releases/{}/ /data/web_static/current".
            format(name)).failed is True:
        return False
    return True


def deploy():
    """Create and distribute an archive to a web server."""
    file = do_pack()
    if file is None:
        return False
    return do_deploy(file)
