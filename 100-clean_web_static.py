#!/usr/bin/python3
"""
A Module that deletes out-of-date archives, using the function do_clean.
"""


env.hosts = ['35.243.129.178', '3.91.29.66']


def do_clean(number=0):
    """
    Deletes out of date archives.
    """
    n = 0
    if number == 0 or number == 1:
        local('ls -A1t ./versions | tail -n +2 | xargs rm')
        run('ls -A1t ./data/web_static/releases | tail -n +2 | xargs rm -rf')
    elif number >= 2:
        n = number + 1
        local('ls -A1t ./versions | tail -n +$n | xargs rm')
        run('ls -A1t ./data/web_static/releases | tail -n +$n | xargs rm -rf')
