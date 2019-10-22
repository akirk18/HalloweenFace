#!usr/bin/python3

import board
import busio
import time
import eyes
import pygame
import digitalio

'''
Eye Positions according to top left corner
[x,x,x,x,x,x,x,x] x
[x,x,0,1,2,x,x,x] 0
[x,0,1,2,3,4,x,x] 1
[x,0,1,2,3,4,x,x] 2
[x,0,1,2,3,4,x,x] 3
[x,x,0,1,x,x,x,x] 4
[x,x,0,1,2,x,x,x] 5
[x,x,x,x,x,x,x,x] x
'''

pygame.init()
file = 'Welcome.mp3'
pygame.mixer.init()


i2c = busio.I2C(board.SCL, board.SDA)
eyes = eyes.Eyes(i2c)
sensor = digitalio.DigitalInOut(board.D4)
sensor.direction = digitalio.Direction.INPUT
btn = digitalio.DigitalInOut(board.D5)
btn.direction = digitalio.Direction.INPUT
btn.pull = digitalio.Pull.DOWN

eyes.Brightness(3)

pygame.mixer.music.load(file)

def Execute(positions, speed):
    for pos in positions:
        pos()
        time.sleep(speed)

look_low_s2s = [eyes.Pos3_0, eyes.Pos3_1, eyes.Pos3_2, eyes.Pos3_3, eyes.Pos3_4,
                eyes.Pos3_3, eyes.Pos3_2]

blink = [eyes.Blink_0, eyes.Blink_1, eyes.Blink_2, eyes.Blink_3, 
         eyes.Blink_4, eyes.Blink_5, eyes.Blink_6, eyes.Blink_7,
         eyes.Blink_8, eyes.Blink_7, eyes.Blink_6, eyes.Blink_5,
         eyes.Blink_4, eyes.Blink_3, eyes.Blink_2, eyes.Blink_1,
         eyes.Blink_0]

close = [eyes.Blink_0, eyes.Blink_1, eyes.Blink_2, eyes.Blink_3,
	 eyes.Blink_4, eyes.Blink_5, eyes.Blink_6, eyes.Blink_7,
	 eyes.Blink_8]

while True:
	if btn.value:
		print("Button Pressed")
		break
	while sensor.value:
		print("Sensor Tripped")
		pygame.mixer.music.play()
		while pygame.mixer.music.get_busy():
  			Execute(blink, 0.05)
  			Execute(look_low_s2s, 0.3)

		Execute(close, 0.05)
		eyes.Shutdown()
print("Goodbye")
eyes.Shutdown()
