#!/usr/bin/env bash
# A script that sets up my web servers for the deployment of web_static.
if ! which nginx > /dev/null 2>&1; then
    sudo apt-get -y update
    sudo apt-get -y install nginx
    sudo service nginx start
fi
sudo mkdir -p /data/
sudo mkdir -p /data/web_static/
sudo mkdir -p /data/web_static/releases/
sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
content="<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolberton School\n\t</body>\n</html>"
#sudo echo "$content" | sudo tee /data/web_static/releases/test/index.html
echo -e "$content" > /data/web_static/releases/test/index.html
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/
config="\\\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current;\n\t}\n"
sudo sed -i "37i $config" /etc/nginx/sites-enabled/default
sudo service nginx restart
