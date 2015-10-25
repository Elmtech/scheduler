#!/bin/bash

if ! [ -e /etc/supervisor/conf.d/$SUPERVISOR_CONF_NAME ] && [ $SUPERVISOR_CONF_PATH ] && [ -e $SUPERVISOR_CONF_PATH ]
  then
    echo "Making symbolic link for " $SUPERVISOR_CONF_PATH
    ln -s $SUPERVISOR_CONF_PATH /etc/supervisor/conf.d/
fi

exec supervisord -n
