#!/bin/bash
# This bash shell script sets up a Banana  PI M2 running Armbian:
# - Get some necessary updates and packages
# - Set keyboard to Hungarian
# - Connects to Wifi and sets a static IP to the device on LAN

echo --- Keyboard config ---
echo "# KEYBOARD CONFIGURATION FILE
# Consult the keyboard(5) manual page.

XKBMODEL=\"pc105\"
XKBLAYOUT=\"hu\"
XKBVARIANT=\"standard\"
XKBOPTIONS=\"lv3:ralt_switch\"

BACKSPACE=\"guess\"" > /etc/default//keyboard

service keyboard-setup restarts
echo Switch keyboard to the set one after each startup
setupcon
sed -i '$i setupcon' /etc/rc.local


echo --- General updates ---
apt update
apt install armbian-config 
apt upgrade
apt dist-upgrade
apt-get install network-manager


echo --- Network config ---
echo Please provide wifi SSID \(name\):
read ssid

echo Please provide wifi password:
read pw

echo Please provide the IP address you want to have on LAN
echo \(Note: You need to know what is available.\)
read ip

echo Trying to set up static IP:
# if ping -c 1 -W 1 ${ip} >/dev/null 2>&1; then
#    echo Requested static IP ${ip} is in use
if true; then
    # Manual connection to Wifi
    echo Simply connecting to wifi $ssid ...
    nmcli dev wifi connect $ssid password $pw

else
    echo IP is available
    echo Setting up static IP
    echo Source: https://docs.armbian.com/User-Guide_Networking/

    apt-get install openvswitch-switch

    rm /etc/netplan/10-dhcp-all-interfaces.yaml

    echo "network:
    version: 2
    renderer: networkd
    ethernets:
      eth0: # Change this to your ethernet interface
        addresses:
        - ${ip}/24
        routes:
        - to: default
          via: 192.168.0.1
        nameservers:
          addresses:
            - 9.9.9.9
            - 1.1.1.1" > /etc/netplan/20-static-ip.yaml

    echo "network:
    version: 2
    renderer: networkd
    wifis:
      $(iw dev | awk '$1=="Interface"{print $2}'):
        dhcp4: true
        dhcp6: true
        access-points:
          \"${ssid}\":
            password: \"${pw}\"" > /etc/netplan/30-wifis-dhcp.yaml

    chmod 600 /etc/netplan/*.yaml

    netplan try
    netplan apply
fi

sleep(2)
reboot
