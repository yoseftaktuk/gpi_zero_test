# from gpiozero import PWMLED
# from time import sleep
# led = PWMLED(17)

# from mfrc522 import MFRC522
# reader = MFRC522() 


# status =  None
# while status != reader.MI_OK:
# 	(status, TagType) = reader.Request(reader.PICC_REQIDL)
# 	if status == reader.MI_OK:
# 		print("Connection Success!")
# from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import time
import datetime
from asyncio import sleep


GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Pull-Up כי פולס = GND

count = 0

def pulse_detected(channel):
        now = datetime.datetime.now()
        global count
        count += 1
        after = datetime.datetime.now()
        print(now= after)
       

def count_coin():
    GPIO.add_event_detect(17, GPIO.FALLING, callback=pulse_detected, bouncetime=50)
    after = datetime.datetime.now()
    print(after)
    try:
        while True:
            sleep(1)
    except KeyboardInterrupt:
        GPIO.cleanup()

count_coin()        


# reader = SimpleMFRC522()

# try:
#     print("Place card...")
#     id, text = reader.read()
#     print("Card ID:", id)
# finally:
#     GPIO.cleanup()


# while True:
#     led.value = 0  # off
#     sleep(1)
#     led.value = 0.2
#     sleep(1)
#     led.value = 0.5  # half brightness
#     sleep(1)
#     led.value = 0.7  # half brightness
#     sleep(1)
#     led.value = 1  # full brightness
#     sleep(1)
# counter = 0
# while True:
#     led.value = counter
#     print(led.value)  # off
#     sleep(0.001)
#     counter += 0.1
#     if counter == 1:
#         counter = 0
