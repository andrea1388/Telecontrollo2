#!/usr/bin/env python2.7
# script by Alex Eames https://raspi.tv
# https://raspi.tv/how-to-use-interrupts-with-python-on-the-raspberry-pi-and-rpi-gpio-part-3
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# GPIO 23 & 17 set up as inputs, pulled up to avoid false detection.
# Both ports are wired to connect to GND on button press.
# So we'll be setting up falling edge detection for both

chan_list = [17,21,22,23,24]
GPIO.setup(chan_list, GPIO.IN)


# now we'll define two threaded callback functions
# these will run in another thread when our events are detected
def my_callback(channel):
    print GPIO.input(21),GPIO.input(22),GPIO.input(23),GPIO.input(24)
    t=GPIO.input(21) + GPIO.input(22)*2 + GPIO.input(23)*4 + GPIO.input(24) *8
    print "Ricevuto tono", t





# when a falling edge is detected on port 17, regardless of whatever 
# else is happening in the program, the function my_callback will be run
GPIO.add_event_detect(17, GPIO.FALLING, callback=my_callback, bouncetime=300)

while True:
    # print GPIO.input(27),GPIO.input(22),GPIO.input(23),GPIO.input(24)
    time.sleep(1)




GPIO.cleanup()           # clean up GPIO on normal exit
