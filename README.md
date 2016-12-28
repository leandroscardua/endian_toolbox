
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
    mv menu-toolbox.pl /home/httpd/menus/main/
    chmod 755 /home/httpd/menus/main/menu-toolbox.pl
    
    curl -Lo toolbox.cgi https://raw.githubusercontent.com/leandroscardua/endian_toolbox/master/toolbox.cgi
    mv toolbox.cgi /home/httpd/cgi-bin/
    chmod 755 /home/httpd/cgi-bin/toolbox.cgi

