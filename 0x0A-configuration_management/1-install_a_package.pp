# this  script to install a package
package {'flask':
  ensure => 'installed',
provider => 'pip3',
}
