#!/usr/bin/python3
"""
Creates and distributes an archive to your web servers,
using the function deploy
"""
import datetime
from fabric.operations import local
from fabric.context_managers import lcd
from fabric.api import local, lcd, put, env, run


env.hosts = ['35.243.129.178', '3.91.29.66']


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


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    fname = archive_path.split('/')[-1]
    r = put(archive_path, "/tmp/")
    if r.failed:
        return False
    path = '/data/web_static/releases/' + fname[:-4]
    r = run('mkdir -p %s' % path)
    if r.failed:
        return False
    r = run('tar -xzf /tmp/%s -C /data/web_static/releases/%s/' %
            (fname, fname[:-4]))
    if r.failed:
        return False
    r = run('rm /tmp/%s' % fname)
    if r.failed:
        return False
    r = run('mv /data/web_static/releases/%s/web_static/*\
    /data/web_static/releases/%s' % (fname[:-4], fname[:-4]))
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/releases/%s/web_static' % fname[:-4])
    if r.failed:
        return False
    r = run('rm -rf /data/web_static/current')
    if r.failed:
        return False
    r = run('ln -s /data/web_static/releases/%s /data/web_static/current'
            % fname[:-4])
    if r.failed:
        return False
    return True


valid_path = None


def deploy():
    """
    Creates and distributes an archive to your web servers.
    """
    global valid_path
    if valid_path is None:
        valid_path = do_pack()
        if valid_path is None:
            return False
    if valid_path is not None:
        return do_deploy(valid_path)
