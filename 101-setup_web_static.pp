# Sets up the web servers for the deployment of web_static using puppet

exec {'/usr/bin/env apt-get update':}
->package {'nginx':
ensure => installed,
}

->file { [ '/data/',
  '/data/web_static/',
  '/data/web_static/releases/',
  '/data/web_static/releases/test/',
  '/data/web_static/shared/', ]:
  ensure => directory,
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

->file {'/data/web_static/releases/test/index.html':
  ensure  => present,
  content => "Nginx Server",
  owner  => 'ubuntu',
  group  => 'ubuntu',
}

->exec {'/usr/bin/env ln -sf /data/web_static/releases/test/ /data/web_static/current':}
->exec {'/usr/bin/env chown -R ubuntu:ubuntu /data/':}

->file_line {'add protocol':
ensure => present,
path   => '/etc/nginx/sites-available/default',
after  => 'listen 80 default_server;',
line   => 'location /hbnb_static/ { alias /data/web_static/current/; autoindex off;}',
require => Package['nginx'],
}

->service { 'nginx':
ensure  => running,
require => Package['nginx'],
}

->exec {'/usr/bin/env service nginx restart':}
