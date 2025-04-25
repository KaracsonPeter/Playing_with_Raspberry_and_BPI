import time

import cv2
import paho.mqtt.client as mqtt


def list_camera_ids(max_ids=10):
    ids = []
    for i in range(max_ids):
        cap = cv2.VideoCapture(i)
        if cap.read()[0]:
            ids.append(i)
        cap.release()
    return ids


cap = cv2.VideoCapture(list_camera_ids()[0], cv2.CAP_V4L2)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'YUYV'))

client = mqtt.Client()
client.connect("192.168.0.129", 1883, 60)

while True:
    ret, frame = cap.read()
    if not ret:
        continue
    _, buf = cv2.imencode('.jpg', frame)
    client.publish("camera/yuyv", buf.tobytes())
