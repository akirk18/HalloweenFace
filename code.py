#!usr/bin/python3

import board
import busio
import time
import eyes
import pygame

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

eyes.Brightness(3)

pygame.mixer.music.load(file)
#pygame.mixer.music.play()
#pygame.event.wait()

def Execute(positions, speed):
    for pos in positions:
        pos
        print(pos)
        time.sleep(speed)

look_low_s2s = [eyes.Pos3_0(), eyes.Pos3_1(), eyes.Pos3_2(), eyes.Pos3_3(), eyes.Pos3_4()]

blink = [eyes.Blink_0(), eyes.Blink_1(), eyes.Blink_2(), eyes.Blink_3(), 
         eyes.Blink_4(), eyes.Blink_5(), eyes.Blink_6(), eyes.Blink_7(),
         eyes.Blink_8()]

pygame.mixer.music.play()
print(pygame.mixer.get_busy())

while (not pygame.mixer.get_busy()):
    Execute(blink, 0.1)
    Execute(look_low_s2s, 0.3)
    print(pygame.mixer.get_busy())

eyes.Shutdown()
	
	
