# Setting up Raspbian on Banana PI M2 Berry (M2U)

## 1. Image
Officially supported images:
https://wiki.banana-pi.org/Banana_Pi_BPI-M2_Berry#Resources
https://drive.google.com/drive/folders/0B_YnvHgh2rwjR0JsaUltalFXanc?resourcekey=0-sP6nS_7yziua5nmCfFQmAw

### These GUI based Raspbian could drive GPIO and PWM:
2017-08-25-raspbian-stretch-preview-bpi-m2u-sd-emmc.img.zip
2020-04-19-raspbian-jessie-bpi-m2u-sd-emmc.img


## 2. Get plug the Banana to a LAN and a monitor

## 3. Enable necessary interfaces through raspi-config
### 3.1. Open terminal with Ctrl + Alt + t
### 3.2. Enable interfaces
```bash
sudo raspi-config
```


## 4. SSH into banana
### 4.1. Get the ip of your eth0 interface
```bash
ip addr
```
### 4.2. Disconnect BPI from monitor & SSH to the IP of eth0
cmd:
```cmd
ssh pi@192.168.x.x 
```

#### User: pi
#### PW: bananapi

## 5. Copy setup.bash file to the BPI by `scp` command

## 6. Run setup.bash

DONE



CANNOT SEE SHIT  
CANNOT FIND APT PACKAGES TO BUILD PYTHON VERSION 3.8.0 FOR ROS NOETIC  
CANNOT FIND BUILT PACKAGES FOR ROS  

---  

MUCH SIMPLER TO GET A RASPBERRY PI 3B+  
THE OLDER THE RASPBERRY THE BETTER IT'S SUPPORT IS






```bash
sudo systemctl enable ssh
sudo systemctl start ssh
echo Checking ssh status:
sudo systemctl status ssh



```


## Extend partition after flashing
```bash
pi@bpi-iot-ros-ai:/dev $ lsblk
NAME        MAJ:MIN RM  SIZE RO TYPE MOUNTPOINT
mmcblk0     179:0    0 14.6G  0 disk
├─mmcblk0p1 179:1    0  256M  0 part /boot
└─mmcblk0p2 179:2    0  6.8G  0 part /

pi@bpi-iot-ros-ai:/dev $ sudo fdisk /dev/mmcblk0

Welcome to fdisk (util-linux 2.29.2).
Changes will remain in memory only, until you decide to write them.
Be careful before using the write command.


Command (m for help): p
Disk /dev/mmcblk0: 14.6 GiB, 15665725440 bytes, 30597120 sectors
Units: sectors of 1 * 512 = 512 bytes
Sector size (logical/physical): 512 bytes / 512 bytes
I/O size (minimum/optimal): 512 bytes / 512 bytes
Disklabel type: dos
Disk identifier: 0x11fd51cd

Device         Boot  Start      End  Sectors  Size Id Type
/dev/mmcblk0p1      204800   729087   524288  256M  c W95 FAT32 (LBA)
/dev/mmcblk0p2      729088 14940159 14211072  6.8G 83 Linux


echo We can extend partition /dev/mmcblk0p2 END from 14940159 to 30597120
sudo apt install cloud-guest-utils

sudo growpart /dev/mmcblk0 2
sudo resize2fs /dev/mmcblk0p2

sudo reboot

echo Check partition free space
df -h
```

## [Python3.9 install](https://www.linuxscrew.com/linux-growpart-fill-disk)
Get CPU version
```bash
pi@bpi-iot-ros-ai:~ $ uname -m
armv7l
```
