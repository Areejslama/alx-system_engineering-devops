# Puppet manifest for configuring Nginx
# This manifest modifies Nginx configuration and restarts the service.

# Define an exec resource to modify Nginx configuration
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/',
  notify  => Exec['nginx-restart'],
}

# Restart Nginx
exec { 'nginx-restart':
  command     => '/etc/init.d/nginx restart',
  path        => '/etc/init.d/',
  refreshonly => true,
}

