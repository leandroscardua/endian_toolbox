
Endian Toolbox
=============
Addon for Endian Firewall 3.2, This tool allows to use : ping, traceroute , dig, nslookup, NMAP and Speedtest on Web Interface, for operation correct it is necessary install NMAP and SpeedTest-Cli, But if you don´t install this item, only ping, traceroute,dig and nslookup are available

Version:
--------
v.1

Requirements/optinal:
--------
- NMAP : https://github.com/leandroscardua/endian_nmap
- Speedtest-cli : https://github.com/sivel/speedtest-cli

Installation:
--------
    curl -Lo menu-toolbox.pl https://raw.githubusercontent.com/leandroscardua/endian_toolbox/master/menu-toolbox.pl
    curl -Lo toolbox.cgi https://raw.githubusercontent.com/leandroscardua/endian_toolbox/master/toolbox.cgi
    mv menu-toolbox.pl /home/httpd/menus/main/
    mv toolbox.cgi /home/httpd/cgi-bin/
    chmod 755 /home/httpd/menus/main/menu-toolbox.pl
    chmod 755 /home/httpd/cgi-bin/toolbox.cgi
        
Or Install all features:
--------
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
    
    Or Install used script
--------
    curl -Lo install.sh https://raw.githubusercontent.com/leandroscardua/endian_toolbox/master/install.sh
    chmod +x install.sh

