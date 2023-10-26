#!/bin/bash

service php7.4-fpm start
chmod 660 /run/php/php7.4-fpm.sock
nginx -g "daemon off;"