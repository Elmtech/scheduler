#!/bin/bash

if [ -f /etc/nginx/conf.d/$APP_ENV_NGINX_CONF_NAME ] && [ $APP_ENV_NGINX_CONF_PATH ] && [ -f $APP_ENV_NGINX_CONF_PATH ]
  then
    echo "Making symbolic link for " $APP_ENV_NGINX_CONF_PATH
    ln -s $APP_ENV_NGINX_CONF_PATH /etc/nginx/conf.d/
fi
