## [MQTT Server on windows](https://www.youtube.com/watch?v=0w5DndNrFg8)
1. [Download mosquitto](https://mosquitto.org/download/)
2. In the installation folder create a config file e.g.: `testconfig.txt` and write the following into it:
```txt
listener 1883

allow_anonymous true
```
3. Close MQTT server from Task Manager if already running
4. Launch a cmd as admin and launch MQTT server by:
```
# cd into your dir where you installed mosquitto and have the created config &&
mosquitto.exe -v -c testconfig.txt
```

### To see messages
1. [Install MQTT explorer](https://mqtt-explorer.com/)
2. Find the IP of your Host PC
```cmd
ipconfig
```
3. Connect to the MQTT server by the MQTT-explorer with your IP.

## MQTT client with your Raspberry
On Raspberry PI  

Save Host PC IP into 'ip' variable
```bash
ip="192.168.0.129"
```

Send message to MQTT server  
```bash
echo Test if MQTT works
sudo apt install mosquitto-clients
mosquitto_pub -h $ip -p 1883 -m "Hello" -t "testPI"
```
OR  
Construct a python file with venv
```bash
mkdir mqtt_test
cd mqtt_test
python3 -m venv venv
source venv/bin/activate
pip3 install paho-mqtt
touch mqtt_msg.py
```

```python
import paho.mqtt.client as mqtt

# Define the MQTT settings
broker_address = "192.168.0.129"  # Replace with your host PC IP
port = 1883  # Default MQTT port
topic = "raspberry_pi_4/test_str"

# Create a new MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_address, port)

# Publish a message
message = "Hello from Raspberry Pi!"
client.publish(topic, message)

print(f"Message '{message}' sent to topic '{topic}'")

# Disconnect from the broker
client.disconnect()
```

And run the script
```bash
python mqtt_msg.py
```

## Troubleshooting (skip)
Host PC
1. Install MQTT server:  
https://mosquitto.org/download/  
OR  
https://mqtt-explorer.com/
Host PC debug
```
# Validate if MQTT is listening on ports
netstat -an | findstr :1883
```

Rapberry debug mqtt
```bash
echo See if PI communicates through port with Host 
sudo apt install nmap
nmap -p 1883 192.168.0.129
```