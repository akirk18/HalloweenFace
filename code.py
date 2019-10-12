#!usr/bin/python3

import board
import busio
import time

from adafruit_ht16k33 import matrix

i2c = busio.I2C(board.SCL, board.SDA)

matrix = matrix.Matrix8x8(i2c)

while True:
	matrix.fill(1)
	time.sleep(5)
	
	for i in range(16):
		matrix.brightness = i
		time.sleep(.5)
	for i in range(4):
		matrix.blink_rate = i
		time.sleep(2)
	
	matrix.blink_rate = 0
	matrix.fill(0)
