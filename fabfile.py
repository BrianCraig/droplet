from time import localtime
from fabric.api import run, cd, local

# example use: $fab -H droplet start

def start():
    run('supervisorctl start all')


def stop():
    run('supervisorctl stop all')
    run('killall python') # asegurarse de cerrar el proceso


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