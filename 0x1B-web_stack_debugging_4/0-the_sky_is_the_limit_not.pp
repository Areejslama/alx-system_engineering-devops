# this mainfest is about setting up server  
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" /etc/nginx/default',
  path    => '/usr/local/bin/:/bin/'
exec ( 'nginx restart':
  command => 'nginx restart',
  path => '/etc/init.d/'
