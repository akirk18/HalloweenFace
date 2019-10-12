'''
Different Eye States
Top:
[7,6,5,4,3,2,1,0] 0
[7,6,5,4,3,2,1,0] 1
[7,6,5,4,3,2,1,0] 2
[7,6,5,4,3,2,1,0] 3
[7,6,5,4,3,2,1,0] 4
[7,6,5,4,3,2,1,0] 5
[7,6,5,4,3,2,1,0] 6
[7,6,5,4,3,2,1,0] 7
'''
from adafruit_ht16k33 import matrix

class EyePostition:
    def __init__(self, i2c):
        self.matrix = matrix.Matrix8x8(i2c)

    '''
    Looking Straight
    '''
    def Straight(self):
        # row 0
        for i in range(8)[2:6]:
            matrix[0,i] = 1
        # row 1
        for i in range(8)[1:7]:
            matrix[1,i] = 1
        # row 2
        for i in range(8):
            matrix[2,i] = 1
        # row 3
        for i in range(8):
            matrix[3,i] = 1
        # row 4
        for i in range(8)[:4]:
            matrix[4,i] = 1
        for i in range(8)[6]:
            matrix[4,i] = 1
        # row 5
        for i in range(8)[:4]:
            matrix[5,i] = 1
        for i in range(8)[6]:
            matrix[5,i] = 1
        # row 6
        for i in range(8)[1:7]:
            matrix[6,i] = 1
        # row 7
        for i in range(8)[2:6]:
            matrix[7,i] = 1
        matrix.show()
        return