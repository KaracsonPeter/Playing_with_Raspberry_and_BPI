# Create and move image to host PC
It is the only way I found to do this ...

Sources:
https://commandmasters.com/commands/v4l2-ctl-linux/

## 1. Plug in webcam to host PC & set it's focus distance in video call

## 2. Plug webcam into Banana PI
### 2.1. See if it recognizes:
```bash
pi@bpi-iot-ros-ai:~ $ ls /dev | grep video
video0
```

### 2.2. See what format the camera supports:
```bash
pi@bpi-iot-ros-ai:~ $ v4l2-ctl --list-formats-ext --device /dev/video0
ioctl: VIDIOC_ENUM_FMT
        Index       : 0
        Type        : Video Capture
        Pixel Format: 'YUYV'
        Name        : YUV 4:2:2 (YUYV)
                Size: Discrete 640x480
                        Interval: Discrete 0.033s (30.000 fps)
                        Interval: Discrete 0.067s (15.000 fps)
                Size: Discrete 352x288
                        Interval: Discrete 0.033s (30.000 fps)
                        Interval: Discrete 0.067s (15.000 fps)
                Size: Discrete 320x240
                        Interval: Discrete 0.033s (30.000 fps)
                        Interval: Discrete 0.067s (15.000 fps)
                Size: Discrete 176x144
                        Interval: Discrete 0.033s (30.000 fps)
                        Interval: Discrete 0.067s (15.000 fps)
                Size: Discrete 160x120
                        Interval: Discrete 0.033s (30.000 fps)
                        Interval: Discrete 0.067s (15.000 fps)
```

### 2.3. Create image

```bash
v4l2-ctl --device=/dev/video0 --set-fmt-video=width=640,height=480,pixelformat=YUYV --stream-mmap --stream-to=test.yuyv --stream-count=1
```

### 2.4. Copy result in host PC cmd:
```cmd
scp pi@192.168.0.80:~/test.yuyv D:\p\RaspberryROS\07_trying_cameras
```

### 2.5. Visualize on host PC
```cmd
python -m venv venv
.\venv\Scripts\activate
pip install opencv-python
python read_imgs.py
```