#increase traffic limit to nginx

exec { 'increase nginx ulimit':
    command => 'sed -i "s/15/4096/" /etc/default/nginx',
    path    => '/usr/local/bin/:/bin/'
}

# restart nginx
-> exec { 'restart nginx':
    command => 'nginx restart',
    path    => '/etc/init.d/'
}
