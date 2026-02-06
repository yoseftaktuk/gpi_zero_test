from gpiozero import PWMLED
from time import sleep
led = PWMLED(17)

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
counter = 0
while True:
    led.value = counter  # off
    sleep(0.001)
    counter += 0.1
    if counter == 1:
        counter = 0