### How to deploy
- Run `cd deployment && docker-compose up -d`
- Get the id of ssh container `deployment_ssh` and exec to bash.
```
$ docker ps -a | grep deployment_ssh
076cd53c1d50        deployment_ssh        "/usr/sbin/sshd -D"      About a minute ago   Up 59 seconds       0.0.0.0:21212->22/tcp         scheduler-ssh        scheduler-ssh

$ docker exec -i -t 076cd53c1d50 bash
```
- Set password for webmaster user `root@d0bf0f43489f:/# passwd webmaster`
- Run `vi /home/webmaster/.ssh/authorized_keys` and your ssh key to server
- Exit from docker container with Ctr+D
- Connect via ssh to container `ssh webmaster@<ip_address> -p 21212`
- Create ssh key for webmaster user `ssh-keygen -t rsa -C 'scheduler.webmaster`
- Add `cat ~/.ssh/id_rsa.pub` to your repository on bitbucket or github
- Clone the project
- Run `cd scheduler/ && cat config/profile/bash_profile.example > ~/.bash_profile`
- Create virtual enviroment `virtualenv env`
- Create `.env` file. See example in `.env.example`
- Exit the ssh and move to `deployment` directory in project
- Run `fab local update` or edit fab file and run update for other machine
- Run `docker-compose restart`
- Application is ready for usage!