#!/bin/sh
# Dynamic Message of the Day (MOTD)
# 
# Add the script call as the last line in /etc/profile 
#
# Last Update: 2020-09-03
# Modified by: Matthias Koterski
#
# To do:
# - Hide Ethernet and WAN IP if not connected.
# - Add weather for Bamberg (or other location).
# - Change Average load in percentage (12%) instead of 0.12
# - Make it beautiful with some nice ASCII art
# 
#
# Change log: 
#
# 0.1e - RAM assigned to ARM and GPU fixed.
# 0.1d - WAN IP fixed.
# 0.1c - Simplified layout.
# 0.1b - Added WiFi IP. WAN IP does not work yet.
# 0.1a - Initial version. Variables are set and displayed.
#
################################################################################################################

# Date and time 1.0
DATE=`date +"%A, %e %B %Y"`

# Hostname 1.0
HOSTNAME=`hostname -f`

# last Login 1.1
LAST1=`last -2 -a | awk 'NR==2{print $3}'` # weekday
LAST2=`last -2 -a | awk 'NR==2{print $5}'` # day
LAST3=`last -2 -a | awk 'NR==2{print $4}'` # month
LAST4=`last -2 -a | awk 'NR==2{print $6}'` # time
# LAST5=`last -2 -a | awk 'NR==2{print $10}'` # remote IP

# Uptime 1.0
UP0=`cut -d. -f1 /proc/uptime`
UP1=$(($UP0/86400)) # Days
UP2=$(($UP0/3600%24)) # Hours
UP3=$(($UP0/60%60)) # Minutes
UP4=$(($UP0%60)) # Seconds

# Average Load 1.0
LOAD1=`cat /proc/loadavg | awk '{print $1}'` # Last minute
#LOAD1PER=`cat /proc/loadavg | awk '{print $1}'` # Last minute load in percent
LOAD2=`cat /proc/loadavg | awk '{print $2}'` # Last 5 Minutes
LOAD3=`cat /proc/loadavg | awk '{print $3}'` # Last 15 Minutes

# Temperature 1.0
TEMP=`vcgencmd measure_temp | cut -c "6-9"`

# Storage 1.0
DISK1=`df -h | grep 'dev/root' | awk '{print $2}'` # Total storage
DISK2=`df -h | grep 'dev/root' | awk '{print $3}'` # Used
DISK3=`df -h | grep 'dev/root' | awk '{print $4}'` # Free

# Memory module 1.2
RAM1=`free --mega | grep 'Mem' | awk '{print $2}'` # Total
RAM2=`free --mega | grep 'Mem' | awk '{print $3}'` # Used
RAM3=`free --mega | grep 'Mem' | awk '{print $4}'` # Free
RAM4=`free --mega | grep 'Swap' | awk '{print $3}'` # Swap used
RAM5=`free --mega | grep 'Swap' | awk '{print $2}'` # Swap total
RAM6=`free --mega | grep 'Swap' | awk '{print $3}'` # Swap used
RAM7=`free --mega | grep 'Swap' | awk '{print $4}'` # Swap free
RAMARM=`vcgencmd get_mem arm | tail -c 5` #ARM MEM
RAMGPU=`vcgencmd get_mem gpu | tail -c 4` #GPU MEM

# Find IP addresses 1.3
if ( ifconfig | grep -q "eth0" ) ; then IP_LAN=`ip addr show eth0 | grep -vw "inet6" | grep "global" | grep -w "inet" | cut -d/ -f1 | awk '{ print $2 }'` ; else IP_LAN="---" ; fi ; #Ethernet IP
if ( ifconfig | grep -q "wlan0" ) ; then IP_WIFI=`ip addr show wlan0 | grep -vw "inet6" | grep "global" | grep -w "inet" | cut -d/ -f1 | awk '{ print $2 }'` ; else IP_WIFI="---" ; fi ; #WiFi IP
IP_WAN=`wget -q -O - http://icanhazip.com/ | tail` #WAN IP

# Weather 0.1


# Plant Section 0.1
# automatic watering activation // automatic watering  N O T  activated !!!
# environmental Temperature
# Location weather
# Number of plants
# Last watering1
# soil moisture1
# soil Temperature1



# Splash 0.1b
# Standard display
echo "
\033[1;36m$DATE
\033[1;32m
\033[0;37mHostname......: \033[1;33m$HOSTNAME
\033[0;37mLast login....: $LAST1, $LAST2 $LAST3 $LAST4
\033[0;37mUptime........: $UP1 days, $UP2:$UP3 hours
\033[0;37mAverage load..: $LOAD1 (1 min) | $LOAD2 (5 min) | $LOAD3 (15 min)
\033[0;37mTemperature...: $TEMP °C
\033[0;37mStorage.......: Total: $DISK1 | Used: $DISK2 | Free: $DISK3
\033[0;37mRAM (MB)......: Total: $RAM1 | Used: $RAM2 | Free: $RAM3
\033[0;37mexternal Swap.: Total: $RAM5 | Used: $RAM6 | Free: $RAM7
\033[0;37mRAM ARM.......: assigned: $RAMARM
\033[0;37mRAM GPU.......: assigned: $RAMGPU
\033[0;37mIPs...........: LAN: \033[1;35m$IP_LAN \033[0;37m| WiFi: \033[1;35m$IP_WIFI\033[0;37m | WAN: \033[1;35m$IP_WAN
\033[m"
