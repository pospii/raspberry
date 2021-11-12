import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
a = 0
while True:
        if GPIO.input(8) and a != 1:
            print("open")
            a = 1


        elif GPIO.input(8) == False and a != 2:
              print("close")
              a = 2
