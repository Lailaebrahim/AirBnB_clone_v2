#!/usr/bin/python3
"""Fabric script  that distributes an archive to your web servers"""
import os
from fabric.api import *


env.host = ['54.174.80.164', '54.161.236.106']
env.user = 'ubuntu'
env.priv_key = '~/etc/.ssh/id_rsa'


def do_deploy(archive_path):
    """
    Method Deploy Web statis Files to web servers
    """

    # Return False if archive doesn't exist
    if not os.path.exists(archive_path):
        return False
    try:
        archive = archive_path.split('/')[-1]
        put(archive_path, '/tmp/{}'.format(archive))
        run('mkdir -p /data/web_static/releases/{}'
            .format(archive.split('.')[0]))
        run('tar -xvzf /tmp/{} -C /data/web_static/releases/{}'
            .format(archive, archive.split('.')[0]))
        run('rm -f /tmp/{}'.format(archive))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{} /data/web_static/current"
            .archive.split('.')[0])
        return True
    except:
        return False
