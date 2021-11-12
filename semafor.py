import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
while(True):
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(14,GPIO.OUT)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(15,GPIO.OUT)
    GPIO.output(18,GPIO.HIGH)
    time.sleep(3)
    GPIO.output(15,GPIO.HIGH)
    time.sleep(2)
    GPIO.output(15,GPIO.LOW)
    GPIO.output(18,GPIO.LOW)

    GPIO.output(14,GPIO.HIGH)

    time.sleep(3)

    GPIO.output(14,GPIO.LOW)
    GPIO.cleanup()
    time.sleep(5)
