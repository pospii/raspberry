import RPi.GPIO as GPIO
import smtplib

GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.IN, pull_up_down = GPIO.PUD_UP)
a = 0
while True:
        if GPIO.input(8) and a != 1:
            print("open")
            a = 1
            server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
            server.login("adam.pospisek@gmail.com", "Zlaterybicky1")
            server.sendmail("adam.pospisek@gmail.com", "adam.pospisek@email.cz", "otevřeno")
            server.quit()



        elif GPIO.input(8) == False and a != 2:
              print("close")
              a = 2
              server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
              server.login("adam.pospisek@gmail.com", "Zlaterybicky1")
              server.sendmail("adam.pospisek@gmail.com", "adam.pospisek@email.cz", "zavřeno")
              server.quit()
