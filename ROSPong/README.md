Task:  
I want to create a ROS 1 project called "RosPong". It contains 2 python scripts. "player_1.py" and "player_2.py". player_1 posts to the topic "scheme_2" and player_2 posts to topic "scheme_1". The sent message is a string "ball". Each player reads it's own topic player_1 reads scheme_1 and player_2 reads scheme_2. After receiving a message (ball), a player waits 1 second and passes the ball back to the topic of the other player.

[Install ROS](https://wiki.ros.org/Installation/Ubuntu)
```bash
sudo bash
sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
apt install curl # if you haven't already installed curl
curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
apt update
apt install ros-noetic-desktop-full

source /opt/ros/noetic/setup.bash
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source ~/.bashrc
apt install python3-rosdep python3-rosinstall python3-rosinstall-generator python3-wstool build-essential
apt install python3-rosdep
rosdep init
rosdep update
```