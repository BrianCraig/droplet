# droplet

instalacion en el servidor  
-------------  

agregar la clave ssh pública de la máquina de desarrollo  

conectar via ssh  

> git clone https://github.com/BrianCraig/droplet.git
> cd droplet
> pip install -r requirements/prod.txt



archivo droplet en /etc/init.d/

	SCRIPT="python /home/droplet/manage.py runserver"
	 
	PIDFILE=/var/run/droplet.pid
	LOGFILE=/var/log/droplet.log
	 
	start() {
	if [ -f /var/run/$PIDNAME ] && kill -0 $(cat /var/run/$PIDNAME); then
	echo 'Service already running' >&2
	return 1
	fi
	echo 'Starting service…' >&2
	local CMD="$SCRIPT &> \"$LOGFILE\" & echo \$!"
	su -c "$CMD" $RUNAS > "$PIDFILE"
	echo 'Service started' >&2
	}
	 
	stop() {
	if [ ! -f "$PIDFILE" ] || ! kill -0 $(cat "$PIDFILE"); then
	echo 'Service not running' >&2
	return 1
	fi
	echo 'Stopping service…' >&2
	kill -15 $(cat "$PIDFILE") && rm -f "$PIDFILE"
	echo 'Service stopped' >&2
	}
	 
	uninstall() {
	echo -n "Are you really sure you want to uninstall this service? That cannot be undone. [yes|No] "
	local SURE
	read SURE
	if [ "$SURE" = "yes" ]; then
	stop
	rm -f "$PIDFILE"
	echo "Notice: log file is not be removed: '$LOGFILE'" >&2
	update-rc.d -f droplet remove
	rm -fv "$0"
	fi
	}
	 
	case "$1" in
	start)
	start
	;;
	stop)
	stop
	;;
	uninstall)
	uninstall
	;;
	restart)
	stop
	start
	;;
	*)
	echo "Usage: $0 {start|stop|restart|uninstall}"
	esac 

> chmod +x /etc/init.d/droplet.sh
> update-rc.d droplet defaults

instalacion en el desarrollo  
-------------  


> git clone https://github.com/BrianCraig/droplet.git
> cd droplet
> pip install -r requirements/dev.txt







