# This manifest sets up a server and applies necessary configurations to Nginx.

# Define an exec resource to modify Nginx configuration
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/nginx/nginx.conf',
  path    => ['/usr/local/bin', '/bin']

exec { 'nginx-restart':
  command => '/etc/init.d/nginx restart',
  path    => ['/sbin', '/usr/sbin', '/bin', '/usr/bin']
}

package { 'nginx':
  ensure => installed,
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  subscribe  => Exec['fix--for-nginx'],
}
