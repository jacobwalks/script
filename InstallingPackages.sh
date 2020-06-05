#!/bin/bash

# Get admin privilages
sudo su -

# install httpd (Linux 2 version)
apt install yum
yum update -y
yum install -y httpd.x86_64
systemctl start httpd.service
systemctl enable httpd.service
echo "Hello World from $(hostname -f)" > /var/www/html/index.html



