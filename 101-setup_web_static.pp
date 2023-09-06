# Sets up the web servers for the deployment of web_static using puppet

exec { '/usr/bin/env apt-get -y update' : }
-> exec { '/usr/bin/env apt-get -y install nginx' : }
-> exec { '/usr/bin/env sudo mkdir -p /data/web_static/releases/test/' : }
-> exec { '/usr/bin/env sudo mkdir -p /data/web_static/shared/' : }
-> exec { '/usr/bin/env echo "Nginx Server" | sudo tee /data/web_static/releases/test/index.html' : }
-> exec { '/usr/bin/env sudo ln -sf /data/web_static/releases/test/ /data/web_static/current' : }
-> exec { '/usr/bin/env sudo chown -R ubuntu:ubuntu /data/' : }
-> exec { '/usr/bin/env sudo sed -i "/listen 80 default_server;/a location /hbnb_static/ { alias /data/web_static/current/; autoindex off;}" /etc/nginx/sites-available/default' : }
-> exec { '/usr/bin/env sudo service nginx restart' : }
