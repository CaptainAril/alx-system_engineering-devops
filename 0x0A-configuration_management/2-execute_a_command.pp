# Kill a process named `Killmenow` using puppet
exec { 'pkill':
  command  => 'pkill killmenow',
  provider => 'shell',
}
