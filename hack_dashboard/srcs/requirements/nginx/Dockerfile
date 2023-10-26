FROM debian:bullseye
EXPOSE 80

RUN apt update
RUN apt upgrade -y

# Install NGINX
RUN apt install nginx php-fpm -y

# Configure NGINX
COPY ./conf/default /etc/nginx/sites-available/
COPY ./scripts/setup.sh /usr/bin/

# Set permissions to website
RUN chmod 755 /var/www/html
RUN chown -R www-data:www-data /var/www/html

ENTRYPOINT ["/bin/sh", "/usr/bin/setup.sh"]