#!/usr/bin/python3
"""
Distributing an archive to your web servers, using the function do_deploy.
"""
from fabric.api import local, lcd, put, env, run
import os.path


env.hosts = ['35.243.129.178', '3.91.29.66']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    """
    if not os.path.exists(archive_path):
        return False
    else:
        fname = archive_path.split('/')[-1]
        put(archive_path, "/tmp/")
        path = '/data/web_static/releases/' + fname[:-4]
        r = run('mkdir -p %s' % path)
        run('tar -xzf /tmp/%s -C /data/web_static/releases/%s/' %
            (fname, fname[:-4]))
        run('rm /tmp/%s' % fname)
        run('mv /data/web_static/releases/%s/web_static/*\
        /data/web_static/releases/%s' % (fname[:-4], fname[:-4]))
        run('rm -rf /data/web_static/releases/%s/web_static' % fname[:-4])
        run('rm -rf /data/web_static/current')
        r = run('ln -s /data/web_static/releases/%s /data/web_static/current'
            % fname[:-4])
        if r.failed:
            return False
        return True
