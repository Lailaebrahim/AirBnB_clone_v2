#!/usr/bin/python3
"""Fabric script  that distributes an archive to your web servers"""
import os
from fabric.api import *

env.hosts = [ '54.174.80.164', '54.161.236.106' ]
env.user = 'ubuntu'



def do_deploy(archive_path):
    """
    """

    # Return False if archive doesn't exist
    if not os.path.exists(archive_path):
        return False

    # Creating the name of the archive using the current date and time
    now = datetime.now()
    archive_name = "web_static_" + now.strftime("%Y%m%d%H%M%S") + ".tgz"

    # Creating the command to generate the archive
    command = "tar -czvf versions/{} web_static".format(archive_name)

    # Executing the command using Fabric's local function
    result = local(command)

    # Checking if the archive has been correctly generated
    if result.failed:
        return None
    else:
        return "versions/{}".format(archive_name)
