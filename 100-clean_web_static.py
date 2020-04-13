#!/usr/bin/python3
"""
A Module that deletes out-of-date archives, using the function do_clean.
"""
from fabric.api import env, lcd, local


env.hosts = ['35.243.129.178', '3.91.29.66']


def do_clean(number=0):
    """
    Deletes out of date archives.
    """
    n = 0
    number = int(number)
    if number == 0:
        n = 2
    else:
        n = number + 1
    with lcd('versions'):
        local('ls -A1t | tail -n +%d | xargs rm' % n)
    with cd('/data/web_static/releases/'):
        run('ls -A1t | tail -n +%d | xargs rm' % n)
