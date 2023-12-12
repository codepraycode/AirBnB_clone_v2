#!usr/bin/env bash
# Setup a webserver for deployment
apt install -y
apt install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<!DOCTYPE html>
<html>
    <head>
        <body>
            <p> Seting up server </p>
        </body>
    </head>
</html>" | tee /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data
sed -i '39 i\ \tlocation /hbnb_static {\n\t\talias /data/web_static/current;\n\t}\n' /etc/nginx/sites-enabled/default
service nginx restart
