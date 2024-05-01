#!/usr/bin/env bash
# this script to puppet http header

exec { 'update system':
  command => '/usr/bin/apt-get update'
}
package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}
file { '/var/www/index/index.html':
  content  => 'Hello world'
}
exec { 'redirect_me':
  command  => 'sed -i "241s/.*/rewrite ^\/redirect_me https:\/\/github.com\/areejslama permanent;/" /etc/nginx/sites-enabled/default',
  path     => '/bin:/usr/bin',
  require  => Package['nginx']
}
exec { 'HTTP header':
  command  => 'sed -i "251s/.*/add_header X-Served-By $HOSTNAME;/" /etc/nginx/sites-enabled/default',
   path     => '/bin:/usr/bin',
  require  => Package['nginx']
}
service { 'nginx':
  ensure  => 'running',
  require => Package['nginx']
}
