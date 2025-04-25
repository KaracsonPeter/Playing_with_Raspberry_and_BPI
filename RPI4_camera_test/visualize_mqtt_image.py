import paho.mqtt.client as mqtt
import cv2
import numpy as np


def on_message(client, userdata, msg):
    np_arr = np.frombuffer(msg.payload, np.uint8)
    img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
    if img is not None:
        cv2.imshow("MQTT Stream", img)
        if cv2.waitKey(1) == 27:  # ESC to exit
            client.disconnect()


client = mqtt.Client()
client.on_message = on_message
client.connect("192.168.0.129", 1883, 60)
client.subscribe("camera/yuyv")
client.loop_forever()
cv2.destroyAllWindows()
