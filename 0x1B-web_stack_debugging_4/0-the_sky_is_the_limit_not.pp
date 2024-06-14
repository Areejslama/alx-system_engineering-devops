# This manifest sets up a server and applies necessary configurations to Nginx.

# Define an exec resource to modify Nginx configuration
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/4096/" etc/default/nginx && sudo service nginx restart' ,
  path    => ['/usr/local/bin', '/bin']
}
