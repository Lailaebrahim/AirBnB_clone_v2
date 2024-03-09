#!/usr/bin/env bash
#Bash script that sets up your web servers for the deployment of web_static.
sudo apt-get -y update
sudo apt-get install -y nginx
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
sudo echo "<!DOCTYPE html>
<html>
    <head>
        <title>Welcome</title>
    </head>
    <body>
        <h1>Welcome to my page!</h1>
        <p>I hope you find what you're looking for.</p>
    </body>
</html> " >> /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
sed -i '50i\\tlocation \/hbnb_static {\n\t\t alias /data/web_static/current;\n\t}' /etc/nginx/sites-available/default
sudo service nginx restart
