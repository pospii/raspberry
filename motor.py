import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)

GPIO.output(15, GPIO.HIGH)
sleep(0.5)
GPIO.output(15, GPIO.LOW)

sleep(2)

GPIO.output(14, GPIO.HIGH)
sleep(0.5)
GPIO.output(14, GPIO.LOW)

GPIO.cleanup()
