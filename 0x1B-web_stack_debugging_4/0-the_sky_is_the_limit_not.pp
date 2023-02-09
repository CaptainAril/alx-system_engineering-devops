file { 'etc/default/nginx':
  content => 'ULIMIT="-n 5000"',
}

