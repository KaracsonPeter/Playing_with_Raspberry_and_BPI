Task:  
I want to create a ROS 1 project called "RosPong". It contains 2 python scripts. "player_1.py" and "player_2.py". player_1 posts to the topic "scheme_2" and player_2 posts to topic "scheme_1". The sent message is a string "ball". Each player reads it's own topic player_1 reads scheme_1 and player_2 reads scheme_2. After receiving a message (ball), a player waits 1 second and passes the ball back to the topic of the other player.

1. [Install ROS](https://wiki.ros.org/Installation/Ubuntu)
```bash
sudo wget -c https://raw.githubusercontent.com/qboticslabs/ros_install_noetic/master/ros_install_noetic.sh && chmod +x ./ros_install_noetic.sh && ./ros_install_noetic.sh
```

2. Create catkin workspace  
(If carkin_make does not work you have to
`source /opt/ros/noetic/setup.bash`)
```bash
mkdir -p ./catkin_ws/src
cd ./catkin_ws
echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
source /opt/ros/noetic/setup.bash
catkin_make
source devel/setup.bash
```

3. Create package
```bash
cd src
catkin_create_pkg ROSPong std_msgs rospy
cd ..
catkin_make
. ./devel/setup.bash
```

4. Create scripts
```bash
cd src
cd ROSPong
mkdir scripts
cd scripts
touch player_1.py
touch player_2.py
chmod +x player_1.py
chmod +x player_2.py
```

Player 1 (catkin_ws/src/ROSPong/scripts/player_1.py)  
```python
import rospy
from std_msgs.msg import String
import time


def main():
	rospy.init_node('player_1', anonymous=True)
	pub = rospy.Publisher('scheme_2', String, queue_size=1)

	pub.publish("ball_0")
	rospy.loginfo("player_1 joined the game!")

	while not rospy.is_shutdown():
    	try:
        	data = rospy.wait_for_message('scheme_1', String, timeout=3)
        	counter = int(data.data.split('_')[-1]) + 1
        	msg = "Players (now player_1) hit the ball " + str(counter) + ". time."
        	rospy.loginfo(msg)
        	time.sleep(1)
        	pub.publish("ball_" + str(counter))
    	except rospy.ROSException:
        	pub.publish("ball_0")


if __name__ == '__main__':
	main()
```

Player 2  
```python
import rospy
from std_msgs.msg import String
import time


def main():
	rospy.init_node('player_2', anonymous=True)
	pub = rospy.Publisher('scheme_1', String, queue_size=1)

	pub.publish("ball_0")
	rospy.loginfo("player_2 joined the game!")

	while not rospy.is_shutdown():
    	data = rospy.wait_for_message('scheme_2', String)
    	counter = int(data.data.split('_')[-1]) + 1
    	msg = "Players (now player_2) hit the ball " + str(counter) + ". time."
    	rospy.loginfo(msg)
    	time.sleep(1)
    	pub.publish("ball_" + str(counter))


if __name__ == '__main__':
	main()

```

Link scripts in CMaleLists of the ROS package  
(catkin_ws/src/ROSPong/CMakeLists.txt)  
Insert these lines to the end:  
```cmake
catkin_install_python(PROGRAMS scripts/player_1.py scripts/player_2.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
```

5. Run the game
Terminal 1
```bash
sudo apt install python3-roslaunch
echo "source /home/karak/p/RaspberryROS/ROSPong/catkin_ws/devel/setup.bash" >> ~/.bashrc
source /home/karak/p/RaspberryROS/ROSPong/catkin_ws/devel/setup.bash
roscd ROSPong
cd ../..
catkin_make
```

Terminal 2
```bash
roscore
```

Terminal 3
```bash
rosrun ROSPong player_1.py
```

Terminal 4
```bash
rosrun ROSPong player_2.py
```
