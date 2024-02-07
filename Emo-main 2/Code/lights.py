#!/usr/bin/python
# -*- coding: UTF-8 -*-
#import chardet

import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode (GPIO.BCM)
GPIO.setup(23, GPIO.OUT, initial=GPIO.LOW)

while True:
    GPIO.output (23, GPIO.HIGH)
 

