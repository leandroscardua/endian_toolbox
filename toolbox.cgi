#!/usr/bin/perl

require 'header.pl';

my %opt;
my @address, @addrs;
my %opt;

&getcgihash(\%opt);

$selected{'TOOL'}{'PING'} = '';
$selected{'TOOL'}{'TRACEROUTE'} = '';
$selected{'TOOL'}{'NMAPS'} = '';
$selected{'TOOL'}{'NMAPP'} = '';
$selected{'TOOL'}{'NMAPA'} = '';
$selected{'TOOL'}{'SPEEDTEST'} = '';
$selected{'TOOL'}{'DIG'} = '';
$selected{'TOOL'}{'NSLOOKUP'} = '';
$selected{'TOOL'}{$opt{'TOOL'}} = 'SELECTED';


&showhttpheaders();

&openpage(_('Toolbox'), 1, '');
&openbox('100%', 'left', _('Ferramentas de Rede'));

print "<FORM METHOD='POST'>\n";

printf <<END

Escolha qual teste deseja executar.<p><p>

END
;

print <<END
<TABLE WIDTH='100%'>
<TR>
<TD WIDTH='15%' CLASS='base'>Selecione: $tr{'toolc'}</TD>
<TD WIDTH='20%'>
<SELECT NAME='TOOL'>
<OPTION VALUE='PING' $selected{'TOOL'}{'PING'}>Ping
<OPTION VALUE='TRACEROUTE' $selected{'TOOL'}{'TRACEROUTE'}>Traceroute
<OPTION VALUE='NMAPS' $selected{'TOOL'}{'NMAPS'}>Nmap Simples
<OPTION VALUE='NMAPP' $selected{'TOOL'}{'NMAPP'}>Nmap All Ports
<OPTION VALUE='NMAPA' $selected{'TOOL'}{'NMAPA'}>Nmap Agressive
<OPTION VALUE='DIG' $selected{'TOOL'}{'DIG'}>Dig
<OPTION VALUE='NSLOOKUP' $selected{'TOOL'}{'NSLOOKUP'}>Nslookup
<OPTION VALUE='SPEEDTEST' $selected{'TOOL'}{'SPEEDTEST'}>SpeedTest
</SELECT>
</TD>
<TD WIDTH='20%' CLASS='base'>IP/Nome/Faixa de Rede:  $tr{'ip addresses or hostnames'}</TD>
<TD WIDTH='30%'><INPUT TYPE='text' SIZE='20' NAME='IP' VALUE='$opt{'IP'}'></TD>
<TD WIDTH='15%' ALIGN='CENTER'><INPUT TYPE='submit' NAME='ACTION' VALUE='Executar'></TD>
</TR>
</TABLE>
END
;

printf <<END
<br class="cb" />
</div>
END
;

&closebox();

if ($opt{'ACTION'} eq "Executar")

{

@address = split(/,/, $opt{'IP'});

&openbox('100%', 'left', _('Console'));
print "<PRE>\n";
if ($opt{'TOOL'} eq 'PING') 
{
system('/bin/ping', '-n', '-c', '5', $opt{'IP'}); 
}
if ($opt{'TOOL'} eq 'TRACEROUTE') 
{
system('/bin/tracepath', '-n', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'NMAPS')
{
system('/usr/bin/nmap', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'NMAPP')
{
system('/usr/bin/nmap', '-p-', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'NMAPA')
{
system('/usr/bin/nmap', '-A', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'DIG')
{
system('/usr/bin/dig', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'NSLOOKUP')
{
system('/usr/bin/nslookup', $opt{'IP'});
}
if ($opt{'TOOL'} eq 'SPEEDTEST')
{
system('/usr/bin/speedtest-cli');
}

print "</PRE>\n";
&closebox();
}

print "</FORM>\n";

&closebox();
&closebigbox();
&closepage();
exit;
