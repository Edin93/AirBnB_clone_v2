# Sets up my web servers for the deployment of web_static.
exec { 'update':
path     => ['/usr/bin', '/usr/sbin', '/bin'],
command  => 'sudo apt-get -y update',
provider => 'shell',
}

package { 'Nginx':
ensure => installed,
}

exec { 'start_nginx':
path     => ['/usr/bin', '/usr/sbin', '/bin'],
command  => 'sudo service nginx start',
provider => 'shell',
}

file { '/data/':
ensure => directory,
}

file { '/data/web_static/':
ensure => directory,
}

file { '/data/web_static/releases/':
ensure => directory,
}

file { '/data/web_static/shared/':
ensure => directory,
}

file { '/data/web_static/releases/test':
ensure => directory,
}

exec { 'fill_index_file':
command  => "echo 'Holberton School' > /data/web_static/releases/test/index.html",
path     => ['/usr/bin', '/usr/sbin', '/bin'],
provider => 'shell',
}

exec { 'created_sym_link':
command  => 'sudo ln -sf /data/web_static/releases/test/ /data/web_static/current',
path     => ['/usr/bin', '/usr/sbin', '/bin'],
provider => 'shell',
}

exec { 'change_data_ownership':
command  => 'sudo chown -R ubuntu:ubuntu /data/',
path     => ['/usr/bin', '/usr/sbin', '/bin'],
provider => 'shell',
}


$old_config='server {'
$new_config="\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n"

exec { 'update_nginx_config':
command  => 'sudo sed -i "s/^$old_config/$old_config$new_config/" /etc/nginx/sites-enabled/default',
path     => ['/usr/bin', '/usr/sbin', '/bin'],
provider => 'shell',
}

exec { 'restart_nginx':
command  => 'sudo service nginx restart',
path     => ['/usr/bin', '/usr/sbin', '/bin'],
provider => 'shell',
}
