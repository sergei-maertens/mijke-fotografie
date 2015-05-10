Apache + mod-wsgi configuration
===============================

An example Apache2 vhost configuration follows:

WSGIDaemonProcess mijke_fotografie-<target> threads=5 maximum-requests=1000 user=<user> group=staff
WSGIRestrictStdout Off

<VirtualHost *:80>
        ServerName my.domain.name

        ErrorLog "/srv/sites/mijke_fotografie/log/apache2/error.log"
        CustomLog "/srv/sites/mijke_fotografie/log/apache2/access.log" common

        WSGIProcessGroup mijke_fotografie-<target>

        Alias /media "/srv/sites/mijke_fotografie/media/"
        Alias /static "/srv/sites/mijke_fotografie/static/"

        WSGIScriptAlias / "/srv/sites/mijke_fotografie/src/mijke_fotografie/wsgi/wsgi_<target>.py"

</VirtualHost>


Nginx + uwsgi + supervisor configuration
========================================

Supervisor/uwsgi:
-----------------

[program:uwsgi-mijke_fotografie-<target>]
user = <user>
command = /srv/sites/mijke_fotografie/env/bin/uwsgi --socket 127.0.0.1:8001 --wsgi-file /srv/sites/mijke_fotografie/src/mijke_fotografie/wsgi/wsgi_<target>.py
home = /srv/sites/mijke_fotografie/env
master = true
processes = 8
harakiri = 600
autostart = true
autorestart = true
stderr_logfile = /srv/sites/mijke_fotografie/log/uwsgi_err.log
stdout_logfile = /srv/sites/mijke_fotografie/log/uwsgi_out.log
stopsignal = QUIT

Nginx
-----

upstream django_mijke_fotografie_<target> {
  ip_hash;
  server 127.0.0.1:8001;
}

server {
  listen :80;
  server_name  my.domain.name;

  access_log /srv/sites/mijke_fotografie/log/nginx-access.log;
  error_log /srv/sites/mijke_fotografie/log/nginx-error.log;

  location /500.html {
    root /srv/sites/mijke_fotografie/src/mijke_fotografie/templates/;
  }
  error_page 500 502 503 504 /500.html;

  location /static/ {
    alias /srv/sites/mijke_fotografie/static/;
    expires 30d;
  }

  location /media/ {
    alias /srv/sites/mijke_fotografie/media/;
    expires 30d;
  }

  location / {
    uwsgi_pass django_mijke_fotografie_<target>;
  }
}
