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
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

count = 0
last_pulse_time = None

def pulse_detected(channel):
    global count
    global last_pulse_time

    count += 1
    last_pulse_time = datetime.datetime.now()

def count_coin():
    global count
    global last_pulse_time

    GPIO.add_event_detect(17, GPIO.FALLING, callback=pulse_detected, bouncetime=5)

    try:
        while True:
            time.sleep(0.05)

            if last_pulse_time is not None:
                delta = datetime.datetime.now() - last_pulse_time

                # אם עברו 200 מילישניות בלי פולס חדש
                if delta > datetime.timedelta(milliseconds=200):

                    print("Finished pulses:", count)

                    if count == 10:
                        print("5 Shekel detected")
                    elif count == 15:
                        print("10 Shekel detected")
                    else:
                        print("Unknown coin")

                    # איפוס לסבב הבא
                    count = 0
                    last_pulse_time = None

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
