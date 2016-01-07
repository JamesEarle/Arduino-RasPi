#!/usr/bin/python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(10, GPIO.IN)
GPIO.setup(14, GPIO.IN)
GPIO.setup(27, GPIO.OUT)

while 1:
	print(GPIO.input(14))
	#GPIO.output(14, GPIO.HIGH)
	#GPIO.output(14, GPIO.LOW)
	time.sleep(0.1)
	print("-")
