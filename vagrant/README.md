Ansible is used to distribute the config file to a server.

The template.j2 is populated from the file myvars and then it's distributed using the ansible playbook mvfile.yml.



----------
Install vagrant

sudo apt-get install vagrant
sudo sh -c "echo 'deb http://download.virtualbox.org/virtualbox/debian '$(lsb_release -cs)' contrib non-free' > /etc/apt/sources.list.d/virtualbox.list" && wget -q http://download.virtualbox.org/virtualbox/debian/oracle_vbox.asc -O- | sudo apt-key add - && sudo apt-get update && sudo apt-get install virtualbox-4.3 dkms


To start the machine go to directory and : vagrant up
To stop the machine go to directory and: vagrant halt

Give access to DB:
mysql -u root -ptest -e "GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'test' WITH GRANT OPTION; FLUSH PRIVILEGES;"
sudo vim /etc/mysql/my.cnf > bind on 0.0.0.0
