#!/usr/bin/python3
"""Fabric script  that distributes an archive to your web servers"""
import os
from fabric.api import run, put, env
env.hosts = ['54.174.80.164', '54.161.236.106']


def do_deploy(archive_path):
    """
    Method Deploy Web statis Files to web servers
    """
    # Return False if archive doesn't exist
    if os.path.exists(archive_path) is False:
        return False
    try:
        archive = archive_path.split('/')[-1]
        archive_no_ext = archive.split('.')[0]
        data_path = '/data/web_static/releases'
        put(archive_path, '/tmp/')
        run('mkdir -p /data/web_static/releases/{}/'
            .format(archive_no_ext))
        run('tar -xzf /tmp/{} -C /data/web_static/releases/{}/'
            .format(archive, archive_no_ext))
        run('rm -f /tmp/{}'.format(archive))
        run('mv {}/{}/web_static/* /data/web_static/releases/{}'
            .format(data_path, archive_no_ext, archive_no_ext))
        run('rm -rf /data/web_static/releases/{}/web_static/'
            .format(archive_no_ext))
        run("rm -rf /data/web_static/current")
        run("ln -sf /data/web_static/releases/{}/  /data/web_static/current"
            .format(archive_no_ext))
        return True
    except:
        return False
