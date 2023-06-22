# Create a Debian 12 Linode with 4 GB Space
apt update
apt install sudo wget gnupg -y
wget -q -O- https://debian.koha-community.org/koha/gpg.asc | sudo apt-key add -
apt update
echo 'deb http://debian.koha-community.org/koha oldstable main' | sudo tee /etc/apt/sources.list.d/koha.list
apt update
apt install koha-common -y
apt install mariadb-server -y
# Edit the /etc/koha/koha-sites.conf as follows
# INTRAPORT="8000"
# OPACPORT="8001"
# DOMAIN="Your-desired-domain
a2enmod rewrite
a2enmod cgi
service apache2 restart
# Edit the /etc/apache2/ports.conf file as follows
# Listen 8000
# Listen 8001
service apache2 restart
koha-create --create-db new-waverly-library
a2enmod headers proxy_http
koha-plack --enable new-waverly-library
koha-plack --start new-waverly-library
service apache2 restart
# View your koha root passwd
koha-passwd new-waverly-library
# Go to the INTRAPORT web UI and log in with `koha_new-waverly-library`:`<revealed-password>`
