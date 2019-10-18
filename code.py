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
pygame.mixer.music.play()
#pygame.event.wait()

#while True:
eyes.Pos0_0()
time.sleep(0.2)
eyes.Pos0_1()
time.sleep(0.2)
eyes.Pos0_2()
time.sleep(0.2)

eyes.Pos1_4()
time.sleep(0.2)
eyes.Pos1_3()
time.sleep(0.2)
eyes.Pos1_2()
time.sleep(0.2)
eyes.Pos1_1()
time.sleep(0.2)
eyes.Pos1_0()
time.sleep(0.2)

eyes.Pos2_0()
time.sleep(0.2)
eyes.Pos2_1()
time.sleep(0.2)
eyes.Pos2_2()
time.sleep(0.2)
eyes.Pos2_3()
time.sleep(0.2)
eyes.Pos2_4()
time.sleep(0.2)

eyes.Pos3_4()
time.sleep(0.2)
eyes.Pos3_3()
time.sleep(0.2)
eyes.Pos3_2()
time.sleep(0.2)
eyes.Pos3_1()
time.sleep(0.2)
eyes.Pos3_0()
time.sleep(0.2)

eyes.Pos4_0()
time.sleep(0.2)
eyes.Pos4_1()
time.sleep(0.2)
eyes.Pos4_2()
time.sleep(0.2)

eyes.Blink_0()
time.sleep(0.1)
eyes.Blink_1()
time.sleep(0.1)
eyes.Blink_2()
time.sleep(0.1)
eyes.Blink_3()
time.sleep(0.1)
eyes.Blink_4()
time.sleep(0.1)
eyes.Blink_5()
time.sleep(0.1)
eyes.Blink_6()
time.sleep(0.1)
eyes.Blink_7()
time.sleep(0.1)
eyes.Blink_8()
time.sleep(0.1)
eyes.Blink_7()
time.sleep(0.1)
eyes.Blink_6()
time.sleep(0.1)
eyes.Blink_5()
time.sleep(0.1)
eyes.Blink_4()
time.sleep(0.1)
eyes.Blink_3()
time.sleep(0.1)
eyes.Blink_2()
time.sleep(0.1)
eyes.Blink_1()
time.sleep(0.1)
eyes.Blink_0()
time.sleep(0.1)

eyes.Shutdown()
	
	
