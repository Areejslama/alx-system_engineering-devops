#!/usr/bin/env bash
# this script to puppet http header

exec { 'update system':
command => '/usr/bin/apt-get update'
}
package { 'nginx':
ensure  => 'present',
require => Exec['update system']
}
file { '/var/www/index/index.html':
content  => 'Hello world'
}
exec { 'redirect_me':
command  => 'sudo sed -i "s/server_name _;/$my_string/"  /etc/nginx/sites-enabled/default',
provider => 'shell'
}
exec { 'HTTP header':
command  => 'sudo sed -i "/server_name _/a add_header X-Served-By $HOSTNAME;" /etc/nginx/sites-enabled/default',
provider => 'shell'
}
service { 'nginx':
ensure  => 'present',
require => package['nginx']
}
