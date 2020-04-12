#!/usr/bin/python3
"""
Generates a .tgz archive from the contents of the web_static folder.
"""
import datetime
from fabric.operations import local
from fabric.context_managers import lcd


def do_pack():
    """
    Generates a .tgz archive from web_static folder.
    """
    local('mkdir -p versions')
    n = datetime.datetime.now()
    ct = str(n.year) + str(n.month) + str(n.day) + str(n.hour) + str(n.minute)
    ct += str(n.second)
    tar_name = 'web_static_' + ct + '.tgz'
    result = local("tar -cvzf versions/%s web_static" % tar_name)
    if (result.failed):
        return None
    else:
        tar_path = 'versions/' + tar_name
        return tar_path
