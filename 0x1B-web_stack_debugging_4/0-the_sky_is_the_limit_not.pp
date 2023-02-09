file { '/etc/default/nginx':
  content => 'ULIMIT="-n 5000"',
  before  => Exec['restart'],
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}

