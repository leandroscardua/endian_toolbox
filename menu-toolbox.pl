#!/usr/bin/perl

my $item = {
    'caption' => _('Toolbox'),
    'enabled' => 1,
    'uri' => '/cgi-bin/toolbox.cgi',
    'title' => _('Toolbox'),
    'helpuri' => 'services.html#tool-box',
};

register_menuitem('02.status', '17.toolbox', $item);

1; 
