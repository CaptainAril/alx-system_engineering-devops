# Modifies the Client SSH configuration file
include stdlib

file_line { 'IdentityFile':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => 'IdentityFile ~/.ssh/school',
  replace => 'true',
}

file_line { 'Password Authentication':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  line    => '   PasswordAuthentication no',
  replace => 'true',
}
