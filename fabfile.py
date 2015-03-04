from time import localtime
from fabric.api import run, cd, local

# example use: $fab -H droplet start

def start():
    run('/etc/init.d/droplet.sh start')


def stop():
    run('/etc/init.d/droplet.sh stop')


def update_local():
    local('git add -u')
    local('git commit -m "automatic commit"')
    local('git push origin master')


def pull():
    with cd('/home/droplet'):
        run('git pull')

def deploy():
    update_local()
    stop()
    pull()
    start()