# -*- coding: utf-8 -*-

from fabric.api import cd, env, run, task
from fabtools.python import virtualenv


@task
def local():
    env.hosts = ['scheduler_local']
    env.user = 'webmaster'
    env.dir = 'scheduler'
    env.path = '/home/{}/{}'.format(env.user, env.dir)
    env.virtualenv = '{}/env'.format(env.path)
    env.repo = 'git@bitbucket.org:Kolyanu4/scheduler.git'
    env.branch = 'master'
    env.django_settings = 'config.settings.production'
    env.server_name = 'Staging'

env.use_ssh_config = True


def manage(command):
    with virtualenv(env.virtualenv):
        with cd(env.path):
            run('python manage.py {} --settings={}'.format(command, env.django_settings))


@task
def update():
    run('git pull origin {}'.format(env.branch))
    with virtualenv(env.virtualenv):
        with cd(env.path):
            run('pip install -r requirements.txt')
            delete_pyc_files()
            collect_static_files()
            synchronise_database()
            apply_migrations()


@task
def collect_static_files(noinput=True, verbosity='0'):
    manage('collectstatic {} --verbosity={}'.format(('--noinput' if noinput else ''), verbosity))


@task
def synchronise_database():
    manage('migrate')


@task
def apply_migrations():
    manage('migrate --no-initial-data --noinput')


def delete_pyc_files():
    with cd(env.path):
        run('find . -name "*.pyc" -exec rm -f {} \;')
