#!/usr/bin/python3
# generates a .tgz archive from the web_static folder of a AirBnB Clone repo
import os.path
from datetime import datetime
from fabric.api import local


def do_pack():
    """Create archive of the content of web_static"""
    dt = datetime.utcnow()
    arc_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(arc_file)).failed is True:
        return None
    return arc_file
