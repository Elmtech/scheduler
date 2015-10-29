#!/bin/bash

function check_previous_command_code {
    if ! [ $? -eq 0 ]; then
        echo "Error with previous command"
        exit -1;
    fi
}

if ! [ -e /data/env/bin/activate ]; then
    echo "Сreating virtualenv..."
    virtualenv /data/env
    check_previous_command_code
    echo "Virtualenv successfully created"
fi

echo "Activate virtualenv and install requirements for the application"
source /data/env/bin/activate
check_previous_command_code
echo "Virtualenv activated"

echo "Installing python requirements"
pip install -r /opt/code/deployment/requirements.txt
check_previous_command_code
echo "Requirements successfully installed"

echo "Run collectstatic"
python /opt/code/manage.py collectstatic --noinput --settings=${SETTINGS_MODULE}
check_previous_command_code
echo "Static files successfully collected"

echo "Run migrations"
python /opt/code/manage.py migrate --fake-initial  --settings=${SETTINGS_MODULE}
check_previous_command_code
echo "Migrations successfully processed"

echo "Starting supervisor"
exec supervisord -n -c /data/supervisor/supervisor.conf
