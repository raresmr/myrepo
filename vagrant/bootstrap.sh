#!/usr/bin/env bash
# configure hosts file for our internal network defined by Vagrantfile
sed -i 's/^mesg n$/tty -s \&\& mesg n/g' /root/.profile

sudo mkdir /var/log/mysql
sudo chown -R mysql:mysql /var/log/mysql
sudo apt-get install software-properties-common
sudo apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db
sudo add-apt-repository 'deb [arch=amd64,i386] http://mariadb.mirror.nucleus.be/repo/10.1/ubuntu trusty main'
sudo apt-get update -y

cat >> /etc/hosts <<EOL

# vagrant environment nodes
10.0.15.10  ub14
EOL
