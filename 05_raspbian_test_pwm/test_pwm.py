import RPi.GPIO as GPIO
import time

PIN = 11  # BCM numbering

GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN, GPIO.OUT)

pwm = GPIO.PWM(PIN, 1000)  # 1kHz frequency

pwm.start(0)  # Duty cycle
for i in range(100):
    pwm.ChangeDutyCycle(i)

    time.sleep(0.01)

pwm.stop()

GPIO.cleanup()
