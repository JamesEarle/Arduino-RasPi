#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17, GPIO.OUT)
GPIO.setup(10, GPIO.IN)

while 1:
	if GPIO.input(10) == False:
		for x in range(0, 150):
			GPIO.output(17, GPIO.HIGH)
			GPIO.output(17, GPIO.LOW)
	else:
		GPIO.output(17, GPIO.LOW)
	time.sleep(0.01)
