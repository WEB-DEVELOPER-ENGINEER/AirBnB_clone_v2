#!/usr/bin/python3
"""
Fabric script that distributes an archive to your web servers
"""
from fabric import Connection, task
from os.path import exists

env = {'hosts': ['34.207.253.78', '3.84.239.44']}

@task
def do_deploy(c, archive_path):
    """distributes an archive to the web servers"""
    if exists(archive_path) is False:
        return False
    try:
        file_name = archive_path.split("/")[-1]
        no_ext = file_name.split(".")[0]
        path = "/data/web_static/releases/"
        for host in env['hosts']:
            conn = Connection(host)
            conn.put(archive_path, '/tmp/')
            conn.run('mkdir -p {}{}/'.format(path, no_ext))
            conn.run('tar -xzf /tmp/{} -C {}{}/'.format(file_name, path, no_ext))
            conn.run('rm /tmp/{}'.format(file_name))
            conn.run('mv {0}{1}/web_static/* {0}{1}/'.format(path, no_ext))
            conn.run('rm -rf {}{}/web_static'.format(path, no_ext))
            conn.run('rm -rf /data/web_static/current')
            conn.run('ln -s {}{}/ /data/web_static/current'.format(path, no_ext))
        return True
    except Exception:
        return False
