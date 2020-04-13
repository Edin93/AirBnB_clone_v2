#!/usr/bin/python3
"""
Distributing an archive to your web servers, using the function do_deploy.
"""
from fabric.api import local, lcd, put, env, run


env.hosts = ['35.243.129.178', '3.91.29.66']


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
