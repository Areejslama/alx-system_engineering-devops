# this  script to install a package
package { 'Werkzeug':
ensure  => '2.1.1',
provider => 'pip3',
}

package { 'flask':
  ensure => 'present',
provider => 'pip3',
}
