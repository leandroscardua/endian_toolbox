#!/bin/sh

cd /tmp/
curl -Lo menu-toolbox.pl https://raw.githubusercontent.com/leandroscardua/endian_toolbox/master/menu-toolbox.pl
curl -Lo toolbox.cgi https://raw.githubusercontent.com/leandroscardua/endian_toolbox/master/toolbox.cgi
curl -Lo nmap.zip https://github.com/leandroscardua/endian_nmap/blob/master/nmap.zip?raw=true
curl -Lo speedtest-cli https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py
mv menu-toolbox.pl /home/httpd/menus/main/
mv toolbox.cgi /home/httpd/cgi-bin/
chmod 755 /home/httpd/menus/main/menu-toolbox.pl
chmod 755 /home/httpd/cgi-bin/toolbox.cgi
chmod +x speedtest-cli
mv speedtest-cli /usr/bin/
unzip -u nmap.zip
cd nmap
cp -R ** /
chmod 755 /usr/bin/nmap
chmod 755 /usr/bin/ndiff
mkdir /lib64
ln -s /lib/ld-linux-x86-64.so.2 /lib64/ld-linux-x86-64.so.2
cd /tmp/
rm -rf nmap.zip
rm -rf nmap 