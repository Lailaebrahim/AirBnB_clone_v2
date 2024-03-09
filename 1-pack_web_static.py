#!/usr/bin/python3
"""Write a Fabric script that generates a .tgz archive
   from the contents of the web_static folder of your 
   AirBnB Clone repo, using the function do_pack"""
import os
from fabric.api import local
from datetime import datetime

def do_pack():
        """
    Function to generate a .tgz archive from the contents of the web_static folder.

    Returns:
    - str:
        The path of the generated archive if it has been correctly generated. Otherwise, it returns None.
    """

    # Creating the versions folder if it doesn't exist
    if not os.path.exists("versions"):
        os.makedirs("versions")

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
