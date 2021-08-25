#!/usr/bin/env bash
# point 0

sudo apt -y update
sudo apt -y upgrate
sudo apt install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

sudo echo "test" > /data/web_static/shared/index.html

ln -sf /data/web_static/releases/test/  /data/web_static/current

sudo chown -hR ubuntu:ubuntu /data/
sudo sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default
sudo service nginx start
