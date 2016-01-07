#!/usr/bin/python
import os
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10, GPIO.IN)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(27, GPIO.OUT)

lights = True

while 1:
	if GPIO.input(10) == False:
		if lights:
			GPIO.output(27, GPIO.LOW)
			GPIO.output(17, GPIO.HIGH)
			lights = False
		else:
			GPIO.output(17, GPIO.LOW)
			GPIO.output(27, GPIO.HIGH)
			lights = True
	else:
		GPIO.output(27, GPIO.LOW)
		GPIO.output(17, GPIO.LOW)

	time.sleep(0.05)	
