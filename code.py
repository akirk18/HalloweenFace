#!usr/bin/python3

import board
import busio
import time
import eyes


i2c = busio.I2C(board.SCL, board.SDA)
eyes = eyes.EyePostition(i2c)

eyes.Straight()