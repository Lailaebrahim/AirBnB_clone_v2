#!/usr/bin/python3
"""Fabric script that archives and distributes web static to your web servers"""
import os
from fabric.api import run, put, env, local
from datetime import datetime
env.hosts = ['54.174.80.164', '54.161.236.106']
tgz_created = None


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.
    Returns:
    - str:
        The path of the archive if it's correctly generated.
        Otherwise, it returns None.
    """
    if not os.path.exists("versions"):
        local("mkdir versions")
    now = datetime.now()
    archive_name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"
    command = "tar -czvf versions/{} web_static".format(archive_name)
    result = local(command)
    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)


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

def deploy():
    """Full Deployment."""
    global tgz_created
    if tgz_created is None:
        tgz_created = do_pack()
    if tgz_created is None:
        return False
    else:
        status = do_deploy(tgz_created)
        return status
