#!/bin/bash

if [ $APP_ENV_NGINX_CONF_PATH ] && [ -e $APP_ENV_NGINX_CONF_PATH ]
    then
        if ! [ -e /etc/nginx/conf.d/$APP_ENV_NGINX_CONF_NAME ]; then
            echo "Making symbolic link for " $APP_ENV_NGINX_CONF_PATH
            ln -s $APP_ENV_NGINX_CONF_PATH /etc/nginx/conf.d/
        else
            echo "Recreating symbolic link!!!"
            rm /etc/nginx/conf.d/$APP_ENV_NGINX_CONF_NAME
            ln -s $APP_ENV_NGINX_CONF_PATH /etc/nginx/conf.d/
        fi
else
    echo "Improperly configured. Can find file" $APP_ENV_NGINX_CONF_PATH "or env variable 'APP_ENV_NGINX_CONF_PATH' is empty"
fi

echo "Starting nginx in foreground mode"
exec nginx -g "daemon off;"
