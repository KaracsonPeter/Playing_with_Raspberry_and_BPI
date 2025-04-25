import numpy as np
import cv2

width, height = 640, 480

with open("test.yuyv", "rb") as f:
    raw = f.read()

frame = np.frombuffer(raw, dtype=np.uint8).reshape((height, width, 2))
bgr = cv2.cvtColor(frame, cv2.COLOR_YUV2BGR_YUYV)

cv2.imshow("YUYV Frame", bgr)
cv2.waitKey(0)
cv2.destroyAllWindows()
