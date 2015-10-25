### How to deploy
1. Run `cd deployment && docker-compose up -d`
2. Get the id of ssh container `deployment_ssh` and exec to bash.
```
$ docker ps -a | grep deployment_ssh
076cd53c1d50        deployment_ssh        "/usr/sbin/sshd -D"      About a minute ago   Up 59 seconds       0.0.0.0:21212->22/tcp         scheduler-ssh        scheduler-ssh

$ docker exec -i -t 076cd53c1d50 bash
```
3. Set password for webmaster user
```
root@d0bf0f43489f:/# passwd webmaster
```
4. Run `vi /home/webmaster/.ssh/authorized_keys` and your ssh key to server
5. Exit from docker container with Ctr+D
6. Connect via ssh to container `ssh webmaster@<ip_address> -p 21212`
7. Create ssh key for webmaster user `ssh-keygen -t rsa -C 'scheduler.webmaster`
8. Add `cat ~/.ssh/id_rsa.pub` to your repository on bitbucket or github
9. Clone the project
10. Run `cd scheduler/ && cat config/profile/bash_profile.example > ~/.bash_profile`
11. Create virtual enviroment
```
virtualenv env
```
12. Create `.env` file. See example in `.env.example`
13. Exit the ssh and move to `deployment` directory in project
14. Run `fab local update` or edit fab file and run update for other machine
15. Run `docker-compose restart`
16. Application is ready for usage!
