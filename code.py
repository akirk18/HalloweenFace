#!usr/bin/python3

import board
import busio
import time
import eyes


i2c = busio.I2C(board.SCL, board.SDA)
eyes = eyes.Eyes(i2c)

eyes.Straight()
time.sleep(5)
eyes.Brightness(12)
time.sleep(2)
eyes.Brightness(3)