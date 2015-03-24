cat << 'EOF' | mysql -u root -p 
CREATE DATABASE wordpress;
CREATE USER wordpressuser@localhost IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON wordpress.* TO wordpressuser@localhost;
FLUSH PRIVILEGES;
exit
EOF
sudo apt-get update
sudo apt-get install php5-gd libssh2-php

