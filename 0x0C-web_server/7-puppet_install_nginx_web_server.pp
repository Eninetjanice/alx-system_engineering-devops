# Install Nginx web server (w/ Puppet)

exec { 'nginx install':
path    => '/usr/bin',
command => 'sudo apt update && sudo apt-get -y install nginx',
}

file { '/var/www/html/index.html':
mode    => '0755',
content => 'Hello World!',
}

exec { 'block server':
path    => '/usr/bin',
command => 'sudo sed -i "/server_name _;/a location /redirect_me {\\n\\trewrite ^\/redirect_me 301 https://www.youtube.com/watch?v=QH2-TGUlwu4; listen 80; \\n\\t}\\n" /etc/nginx/sites-enabled/default; sudo service nginx restart',
}

exec { 'Restart nginx':
path    => '/usr/bin',
command => 'sudo service nginx restart',
}
