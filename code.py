#!usr/bin/python3

import board
import busio
import time
import eyes


i2c = busio.I2C(board.SCL, board.SDA)
eyes = eyes.Eyes(i2c)

eyes.Brightness(3)
eyes.Straight()