# WANIP

myip="$(dig +short myip.opendns.com @resolver1.opendns.com)"
echo "My WAN/Public IP address: ${myip}"


pi@raspby01:/ $ host myip.opendns.com resolver1.opendns.com
Using domain server:
Name: resolver1.opendns.com
Address: 208.67.222.222#53
Aliases: 

myip.opendns.com has address 217.61.154.58
Host myip.opendns.com not found: 3(NXDOMAIN)
Host myip.opendns.com not found: 3(NXDOMAIN)

echo -n `host myip.opendns.com resolver1.opendns.com | tail -c 10` #useless
NXDOMAIN)






Text Extraction!!!

echo -n $foo | tail -c 3

echo -n `hostname | tail -c 4`


-------

textract.txt
/some/random/file.csv:some string
/some/random/file2.csv:some string2
123M
64M


Code: vcgencmd get_mem arm 
Return: arm=948M

sed -e 's/Here\(.*\)String/\1/'

vcgencmd get_mem arm | sed -e 's/arm=\(.*\)M/\1/'
| sed -e 's/gpu=\(.*\)M/\1/'

cut -d "=" -f2- <<< `vcgencmd get_mem gpu`

sed -e 's#.*arm=\(\)#\1#' <<< `vcgencmd get_mem arm`

return number before character in string linux






WEATHER

Weather............: `curl -s "http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|UK|UK001|NAILSEA|" | sed -n '/Currently:/ s/.*: \(.*\): \([0-9]*\)\([CF]\).*/\2°\3, \1/p'`



https://weather.codes/germany/
Weather Location Codes/IDs for Germany
Below are the weather location codes for Germany used by AOL Weather, The Weather Channel (weather.com), Yahoo! Weather and others.

Bamberg
GMXX0005

Ferdinandshof
GMXX2113

Wanne-Eickel
GMXX7305



IP addresses

pi@raspby01:~ $ ip addr show eth0
2: eth0: <NO-CARRIER,BROADCAST,MULTICAST,UP> mtu 1500 qdisc mq state DOWN group default qlen 1000
    link/ether dc:a6:32:29:60:14 brd ff:ff:ff:ff:ff:ff
pi@raspby01:~ $ ip addr show wlan0
3: wlan0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
    link/ether dc:a6:32:29:60:16 brd ff:ff:ff:ff:ff:ff
    inet 192.168.1.111/24 brd 192.168.1.255 scope global dynamic noprefixroute wlan0
       valid_lft 863754sec preferred_lft 755754sec
    inet6 fe80::4ffb:a429:8d62:571c/64 scope link 
       valid_lft forever preferred_lft forever
