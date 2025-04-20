# 0. Get a decent SD card. (Good to have 2 SD card readers in case one of them fails (it might be suck to realize this fact...).)

# 1. [Choosing Armbian for Banana PI](https://www.armbian.com/download/?device_support=Standard%20support)
  Your CPU type defines what OS you'll need. I have A40i-H which is an [alternative version of R40 and V40](https://forum.armbian.com/topic/15875-installing-armbian-on-a40i/).  
  Therefore:

## 1.2 [Download correct Operating System image](https://www.armbian.com/bananapi-m2u/)
## 1.2 [Etcher will help you flash your SD card](https://etcher.balena.io/#download-etcher)
  (After plugged into your PC which is responsible for flashing it.)
## 1.3 Plug the flashed SD card into your Banana to get started
Create account, etc... Get into your first shell in the OS.

# 2. Setting up things
## 2.1 Keyboard:
For me:  
 - Go to keyboard config:
  ```bash
  sudo dpkg-reconfigure keyboard-configuration
  ```  
  Chose your favorite options.
 - Restart keyboard service:
  ```bash
  sudo service keyboard-setup restart
  ```
 - Set keyboard to chosen:
  ```bash
  sudo setupcon
  ```

## 2.2
useful links:  
nmcli: command not found + help menu: https://www.thegeekdiary.com/nmcli-command-not-found/
  ```bash
  host=alma-wifi
  pw=1234

  sudo apt update
  sudo apt install armbian-config 
  sudo apt upgrade
  sudo apt dist-upgrade
  echo Connecting to provided network option ...
  sudo apt-get install network-manager
  nmcli dev wifi connect $host password $pw

  echo Configure OS
  sudo armbian-config
  echo Restart device
  sudo reboot
  echo Shot down device
  sudo poweroff
  ```