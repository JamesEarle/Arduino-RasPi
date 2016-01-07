#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

lights = True

while 1:	
	if lights:
		GPIO.output(27, GPIO.LOW)
		GPIO.output(17, GPIO.HIGH)
		lights = False
	else:
		GPIO.output(17, GPIO.LOW)
		GPIO.output(27, GPIO.HIGH)
		lights = True

	time.sleep(0.3)
