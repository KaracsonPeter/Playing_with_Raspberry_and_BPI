# 0. Get a decent SD card. (Good to have 2 SD card readers in case one of them fails (it might be suck to realize this fact...).)

# 1. [Choosing Armbian for Banana PI](https://www.armbian.com/download/?device_support=Standard%20support)
  Your CPU type defines what OS you'll need. I have A40i-H which is an [alternative version of R40 and V40](https://forum.armbian.com/topic/15875-installing-armbian-on-a40i/).  
  Therefore:

## 1.2 [Download correct Operating System image](https://www.armbian.com/bananapi-m2u/)
## 1.2 [Etcher will help you flash your SD card](https://etcher.balena.io/#download-etcher)
  (After plugged into your PC which is responsible for flashing it.)
## 1.3 Plug the flashed SD card into your Banana to get started
Connect Banana to a monitor and to ethernet with a cable for the first startup.
Create account, etc... Get into your first shell in the OS.

## 1.4 Run setup.bash
1. Open a Git bash in "banana_pi_getting_started" dir (if you are on windows, else just a bash on host) and write the following:
```bash
scp setup.bash root@bananapim2ultra:/root/
```
2. Run the shell script
```bash
bash setup.py
```
3. Press Y everywhere and provide the correct wifi credentials, otherwise you'll need to connect manually by:
```bash
nmcli dev wifi connect MY_SSID password MY_PW
```




## 2.2
1. Connect Banana to a monitor for first startup ethernet
2. SSH into it (have to find it's IP)

Links:  
nmcli: command not found + help menu: https://www.thegeekdiary.com/nmcli-command-not-found/
i2c: https://sigmdel.ca/michel/ha/opi/opipc2_i2c_en.html#i2c0
https://forum.banana-pi.org/t/banana-pi-bpi-m4-how-to-get-i2c-and-spi-running-tutorial/12824
https://www.cnblogs.com/schips/p/porting_i2c-tools_on_arm_linux_with_usage.html
armbianip: https://github.com/bitbank2/ArmbianIO/tree/master

static IP:
https://docs.armbian.com/User-Guide_Networking/

idk:
https://wiki.banana-pi.org/Banana_Pi_BPI-M2_Berry#Image_Release
https://wiki.banana-pi.org/%E9%A6%99%E8%95%89%E6%B4%BE_BPI-M2_Berry
https://forum.banana-pi.org/t/how-to-connect-my-audio-card-with-i2s/6324/6
https://thepihut.com/blogs/raspberry-pi-tutorials/gpio-and-python-39-blinking-led
https://github.com/blackzspace-de-Tutorials/How-To-Control-GPIO-BPI-M2-Berry
https://github.com/BPI-SINOVOIP/BPI-M4-bsp
https://www.electronicsdatasheets.com/datasheet/Banana%20Pi%20M2%20Berry%20user%20guide.pdf
https://wiki.ros.org/Installation


Cheat sheet and useful commands
```bash
echo Configure OS
sudo armbian-config
echo Restart device
sudo reboot
echo Shot down device
sudo poweroff
```

#### Shits I have tried:
```bash
```bash
host=alma-wifi
pw=1234
local_ip="192.168.1.100"

sudo apt update
sudo apt install armbian-config 
sudo apt upgrade
sudo apt dist-upgrade
echo Connecting to provided network option ...
sudo apt-get install network-manager
nmcli dev wifi connect $host password $pw


sudo nmcli con mod $host ipv4.addresses "$local_ip/24" ipv4.gateway "192.168.1.1" ipv4.dns "8.8.8.8" ipv4.method manual
sudo systemctl enable ssh
sudo systemctl start ssh
echo Get IP Address
ip address
conn_name=$(nmcli con show | grep wifi | awk '{print $1}')
nmcli con mod $conn_name ipv4.addresses 192.168.1.100/24
nmcli con mod $conn_name ipv4.gateway 192.168.1.1
nmcli con mod $conn_name ipv4.dns "8.8.8.8 8.8.4.4"
nmcli con mod $conn_name ipv4.method manual
nmcli con up $conn_name

echo ???
apt-get install openvswitch-switch
```