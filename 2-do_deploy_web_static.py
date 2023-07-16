#!/usr/bin/env python3

"""
Fabric script to deploy an archive to web servers.
"""

import os
import datetime
from fabric.api import env, put, run, cd
from fabric.contrib.files import exists

# Set the web server IP addresses
env.hosts = ["35.243.225.26", "34.75.87.53"]

# Set the remote directory for storing the archive
env.remote_dir = "/data/web_static/releases/"

# Set the name of the archive file
env.archive_name = "web_static"

# Set the directory for storing error logs
env.error_log_dir = os.path.join(
    os.path.dirname(os.path.abspath(__file__)), "logs"
)

def _get_timestamp():
    """Get the current timestamp in the format YYYYMMDDHHMMSS"""

    now = datetime.datetime.now()
    return now.strftime("%Y%m%d%H%M%S")

def _get_remote_archive_path():
    """Get the path to the remote archive file"""

    timestamp = _get_timestamp()
    return os.path.join(env.remote_dir, env.archive_name + "_" + timestamp + ".tgz")

def _create_remote_dir():
    """Create the remote directory for storing the archive"""

    run("sudo mkdir -p {}".format(env.remote_dir))

def _upload_archive(archive_path):
    """Upload the archive to the remote server"""

    remote_archive_path = _get_remote_archive_path()
    put(archive_path, remote_archive_path)
    return remote_archive_path

def _extract_archive(remote_archive_path):
    """Extract the archive on the remote server"""

    remote_dir = os.path.join(
        env.remote_dir, os.path.splitext(os.path.basename(remote_archive_path))[0]
    )

    run("sudo mkdir -p {}".format(remote_dir))
    with cd(remote_dir):
        run("sudo tar -xzf {}".format(remote_archive_path))

    return remote_dir

def _create_symlink(remote_dir):
    """Create a symbolic link to the new release"""

    run("sudo rm -f /data/web_static/current")
    run("sudo ln -s {} /data/web_static/current".format(remote_dir))

def deploy(archive_path):
    """Deploy the archive to the web servers"""

    if not os.path.exists(archive_path):
        print("ERROR: Archive file not found: {}".format(archive_path))
        return False

    try:
        # Create the remote directory for storing the archive
        _create_remote_dir()

        # Upload the archive to the remote server
        remote_archive_path = _upload_archive(archive_path)

        # Extract the archive on the remote server
        remote_dir = _extract_archive(remote_archive_path)

        # Create a symbolic link to the new release
        _create_symlink(remote_dir)

        print("Deployment successful!")
        return True

    except Exception as e:
        error_log_path = os.path.join(
            env.error_log_dir, "deploy_error_{}.log".format(_get_timestamp())
        )
        with open(error_log_path, "w") as f:
            f.write(str(e))
        print("ERROR: Deployment failed. See {} for details.".format(error_log_path))
        return False
