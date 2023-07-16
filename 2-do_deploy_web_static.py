#!/usr/bin/python3
"""Distributes an archive to web servers"""
from fabric.api import env, run, put, cd, sudo
from os.path import basename, join, splitext, exists
env.hosts = ['34.207.253.78', '3.84.239.44']


def do_deploy(archive_path):
    """Distributes an archive to web servers"""
    if not exists(archive_path):
        return False
    file_name = basename(archive_path)
    no_ext = splitext(file_name)[0]
    path = '/data/web_static/releases/'
    with cd('/tmp'):
        put(archive_path, './')
    with cd(path):
        sudo('mkdir -p {}/{}'.format(path, no_ext))
        sudo('tar -xzf /tmp/{} -C {}/{}'.format(file_name, path, no_ext))
        sudo('rm -f /tmp/{}'.format(file_name))
        with cd('{}/{}'.format(path, no_ext)):
            sudo('mv web_static/* .')
            sudo('rm -rf web_static')
    with cd('/data/web_static'):
        sudo('rm -f current')
        sudo('ln -sf {}/{} current'.format(path, no_ext))
    return True
