from fabric.api import run, cd

# example use: $fab -H droplet start

def start():
    run('/etc/init.d/droplet.sh start')

def stop():
    run('/etc/init.d/droplet.sh stop')

def pull():
    with cd('/home/droplet'):
        run('git pull')
