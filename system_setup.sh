# Create a Debian 12 Linode with 4 GB Space
apt update && apt upgrade -y
apt install sudo wget gnupg -y
wget -q -O- https://debian.koha-community.org/koha/gpg.asc | sudo apt-key add -
apt update
echo 'deb http://debian.koha-community.org/koha stable main' | sudo tee /etc/apt/sources.list.d/koha.list
apt update
apt install koha-common mariadb-server -y

# Edit the /etc/koha/koha-sites.conf as follows
# INTRAPORT="80"
# INTRASUFFIX="-admin"
# OPACPORT="80"
# DOMAIN=".newwaverlypubliclibrary.org/"
cp /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-available/koha-ssl.conf
a2enmod ssl
a2dissite default-ssl.conf
a2ensite koha-ssl.conf
a2enmod rewrite
a2enmod cgi
service apache2 restart

koha-create --create-db koha
a2enmod headers proxy_http
koha-plack --enable koha
koha-plack --start koha
service apache2 restart

# Edit the /etc/apache2/sites-available/koha-ssl.conf as follows
# OPAC

# <VirtualHost *:443>
# 	<IfVersion >= 2.4>
# 		Define instance "koha"
# 	</IfVersion>
# 	Include /etc/koha/apache-shared.conf
# 	#  Include /etc/koha/apache-shared-disable.conf
# 	Include /etc/koha/apache-shared-opac-plack.conf
# 	Include /etc/koha/apache-shared-opac.conf

# 	ServerName koha.newwaverlypubliclibrary.org
# 	SetEnv KOHA_CONF "/etc/koha/sites/koha/koha-conf.xml"
# 	AssignUserID koha-koha koha-koha

# 	ErrorLog    /var/log/koha/koha/opac-error.log
# 	#  TransferLog /var/log/koha/koha/opac-access.log

# 	SSLEngine on
# 	SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
# 	SSLCertificateKeyFile   /etc/ssl/private/ssl-cert-snakeoil.key
# 	<FilesMatch "\.(?:cgi|shtml|phtml|php)$">
# 		SSLOptions +StdEnvVars
# 	</FilesMatch>
# 	<Directory /usr/lib/cgi-bin>
# 		SSLOptions +StdEnvVars
# 	</Directory>
# </VirtualHost>

# # Intranet
# <VirtualHost *:443>
#   <IfVersion >= 2.4>
#    Define instance "koha"
#   </IfVersion>
# 	Include /etc/koha/apache-shared.conf
# 	#  Include /etc/koha/apache-shared-disable.conf
# 	Include /etc/koha/apache-shared-intranet-plack.conf
# 	Include /etc/koha/apache-shared-intranet.conf

# 	ServerName koha-admin.newwaverlypubliclibrary.org
# 	SetEnv KOHA_CONF "/etc/koha/sites/koha/koha-conf.xml"
# 	AssignUserID koha-koha koha-koha

# 	ErrorLog    /var/log/koha/koha/intranet-error.log
# 	#  TransferLog /var/log/koha/koha/intranet-access.log

# 	SSLEngine on
# 	SSLCertificateFile      /etc/ssl/certs/ssl-cert-snakeoil.pem
# 	SSLCertificateKeyFile   /etc/ssl/private/ssl-cert-snakeoil.key
# 	<FilesMatch "\.(?:cgi|shtml|phtml|php)$">
# 		SSLOptions +StdEnvVars
# 	</FilesMatch>
# 	<Directory /usr/lib/cgi-bin>
# 		SSLOptions +StdEnvVars
# 	</Directory>
# </VirtualHost>

# View your koha root passwd
koha-passwd koha
# Go to the INTRAPORT web UI and log in with `koha_koha`:`<revealed-password>`
