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

class Eyes:
    def __init__(self, i2c, brightness=7):
        self.matrix = matrix.Matrix8x8(i2c)
        self.Brightness(brightness)
    
    '''
    Define the brightness
    '''
    def Brightness(self, brightness):
        self.matrix.brightness = brightness
        return
    
    '''
    Looking Straight
    '''
    def Center(self):
        # row 0
        self.matrix[0,0] = 0
        self.matrix[0,1] = 0
        self.matrix[0,2] = 1
        self.matrix[0,3] = 1
        self.matrix[0,4] = 1
        self.matrix[0,5] = 1
        self.matrix[0,6] = 0
        self.matrix[0,7] = 0
        # row 1
        self.matrix[1,0] = 0
        self.matrix[1,1] = 1
        self.matrix[1,2] = 1
        self.matrix[1,3] = 1
        self.matrix[1,4] = 1
        self.matrix[1,5] = 1
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 1
        self.matrix[2,3] = 1
        self.matrix[2,4] = 1
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 1
        self.matrix[3,4] = 1
        self.matrix[3,5] = 1
        self.matrix[3,6] = 1
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 1
        self.matrix[4,2] = 1
        self.matrix[4,3] = 0
        self.matrix[4,4] = 0
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
        self.matrix[5,3] = 0
        self.matrix[5,4] = 0
        self.matrix[5,5] = 1
        self.matrix[5,6] = 1
        self.matrix[5,7] = 1
        # row 6
        self.matrix[6,0] = 0
        self.matrix[6,1] = 1
        self.matrix[6,2] = 1
        self.matrix[6,3] = 1
        self.matrix[6,4] = 1
        self.matrix[6,5] = 1
        self.matrix[6,6] = 1
        self.matrix[6,7] = 0
        # row 7
        self.matrix[7,0] = 0
        self.matrix[7,1] = 0
        self.matrix[7,2] = 1
        self.matrix[7,3] = 1
        self.matrix[7,4] = 1
        self.matrix[7,5] = 1
        self.matrix[7,6] = 0
        self.matrix[7,7] = 0
        self.matrix.show()
        return

    '''
    Looking Left
    '''
    def Left(self):
        # row 0
        self.matrix[0,0] = 0
        self.matrix[0,1] = 0
        self.matrix[0,2] = 1
        self.matrix[0,3] = 1
        self.matrix[0,4] = 1
        self.matrix[0,5] = 1
        self.matrix[0,6] = 0
        self.matrix[0,7] = 0
        # row 1
        self.matrix[1,0] = 0
        self.matrix[1,1] = 1
        self.matrix[1,2] = 1
        self.matrix[1,3] = 1
        self.matrix[1,4] = 1
        self.matrix[1,5] = 1
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 1
        self.matrix[2,3] = 1
        self.matrix[2,4] = 1
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 1
        self.matrix[3,4] = 1
        self.matrix[3,5] = 1
        self.matrix[3,6] = 1
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 0
        self.matrix[4,2] = 0
        self.matrix[4,3] = 1
        self.matrix[4,4] = 1
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 0
        self.matrix[5,2] = 0
        self.matrix[5,3] = 1
        self.matrix[5,4] = 1
        self.matrix[5,5] = 1
        self.matrix[5,6] = 1
        self.matrix[5,7] = 1
        # row 6
        self.matrix[6,0] = 0
        self.matrix[6,1] = 1
        self.matrix[6,2] = 1
        self.matrix[6,3] = 1
        self.matrix[6,4] = 1
        self.matrix[6,5] = 1
        self.matrix[6,6] = 1
        self.matrix[6,7] = 0
        # row 7
        self.matrix[7,0] = 0
        self.matrix[7,1] = 0
        self.matrix[7,2] = 1
        self.matrix[7,3] = 1
        self.matrix[7,4] = 1
        self.matrix[7,5] = 1
        self.matrix[7,6] = 0
        self.matrix[7,7] = 0
        self.matrix.show()
        return

    '''
    Looking Right
    '''
    def Right(self):
        # row 0
        self.matrix[0,0] = 0
        self.matrix[0,1] = 0
        self.matrix[0,2] = 1
        self.matrix[0,3] = 1
        self.matrix[0,4] = 1
        self.matrix[0,5] = 1
        self.matrix[0,6] = 0
        self.matrix[0,7] = 0
        # row 1
        self.matrix[1,0] = 0
        self.matrix[1,1] = 1
        self.matrix[1,2] = 1
        self.matrix[1,3] = 1
        self.matrix[1,4] = 1
        self.matrix[1,5] = 1
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 1
        self.matrix[2,3] = 1
        self.matrix[2,4] = 1
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 1
        self.matrix[3,4] = 1
        self.matrix[3,5] = 1
        self.matrix[3,6] = 1
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 1
        self.matrix[4,2] = 1
        self.matrix[4,3] = 1
        self.matrix[4,4] = 1
        self.matrix[4,5] = 0
        self.matrix[4,6] = 0
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
        self.matrix[5,3] = 1
        self.matrix[5,4] = 1
        self.matrix[5,5] = 0
        self.matrix[5,6] = 0
        self.matrix[5,7] = 1
        # row 6
        self.matrix[6,0] = 0
        self.matrix[6,1] = 1
        self.matrix[6,2] = 1
        self.matrix[6,3] = 1
        self.matrix[6,4] = 1
        self.matrix[6,5] = 1
        self.matrix[6,6] = 1
        self.matrix[6,7] = 0
        # row 7
        self.matrix[7,0] = 0
        self.matrix[7,1] = 0
        self.matrix[7,2] = 1
        self.matrix[7,3] = 1
        self.matrix[7,4] = 1
        self.matrix[7,5] = 1
        self.matrix[7,6] = 0
        self.matrix[7,7] = 0
        self.matrix.show()
        return

    '''
    Looking Transition Left
    '''
    def MidLeft(self):
        # row 0
        self.matrix[0,0] = 0
        self.matrix[0,1] = 0
        self.matrix[0,2] = 1
        self.matrix[0,3] = 1
        self.matrix[0,4] = 1
        self.matrix[0,5] = 1
        self.matrix[0,6] = 0
        self.matrix[0,7] = 0
        # row 1
        self.matrix[1,0] = 0
        self.matrix[1,1] = 1
        self.matrix[1,2] = 1
        self.matrix[1,3] = 1
        self.matrix[1,4] = 1
        self.matrix[1,5] = 1
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 1
        self.matrix[2,3] = 1
        self.matrix[2,4] = 1
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 1
        self.matrix[3,4] = 1
        self.matrix[3,5] = 1
        self.matrix[3,6] = 1
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 1
        self.matrix[4,2] = 0
        self.matrix[4,3] = 0
        self.matrix[4,4] = 1
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 0
        self.matrix[5,3] = 0
        self.matrix[5,4] = 1
        self.matrix[5,5] = 1
        self.matrix[5,6] = 1
        self.matrix[5,7] = 1
        # row 6
        self.matrix[6,0] = 0
        self.matrix[6,1] = 1
        self.matrix[6,2] = 1
        self.matrix[6,3] = 1
        self.matrix[6,4] = 1
        self.matrix[6,5] = 1
        self.matrix[6,6] = 1
        self.matrix[6,7] = 0
        # row 7
        self.matrix[7,0] = 0
        self.matrix[7,1] = 0
        self.matrix[7,2] = 1
        self.matrix[7,3] = 1
        self.matrix[7,4] = 1
        self.matrix[7,5] = 1
        self.matrix[7,6] = 0
        self.matrix[7,7] = 0
        self.matrix.show()
        return

    '''
    Looking Transition Right
    '''
    def MidRight(self):
        # row 0
        self.matrix[0,0] = 0
        self.matrix[0,1] = 0
        self.matrix[0,2] = 1
        self.matrix[0,3] = 1
        self.matrix[0,4] = 1
        self.matrix[0,5] = 1
        self.matrix[0,6] = 0
        self.matrix[0,7] = 0
        # row 1
        self.matrix[1,0] = 0
        self.matrix[1,1] = 1
        self.matrix[1,2] = 1
        self.matrix[1,3] = 1
        self.matrix[1,4] = 1
        self.matrix[1,5] = 1
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 1
        self.matrix[2,3] = 1
        self.matrix[2,4] = 1
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 1
        self.matrix[3,4] = 1
        self.matrix[3,5] = 1
        self.matrix[3,6] = 1
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 1
        self.matrix[4,2] = 1
        self.matrix[4,3] = 1
        self.matrix[4,4] = 0
        self.matrix[4,5] = 0
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
        self.matrix[5,3] = 1
        self.matrix[5,4] = 0
        self.matrix[5,5] = 0
        self.matrix[5,6] = 1
        self.matrix[5,7] = 1
        # row 6
        self.matrix[6,0] = 0
        self.matrix[6,1] = 1
        self.matrix[6,2] = 1
        self.matrix[6,3] = 1
        self.matrix[6,4] = 1
        self.matrix[6,5] = 1
        self.matrix[6,6] = 1
        self.matrix[6,7] = 0
        # row 7
        self.matrix[7,0] = 0
        self.matrix[7,1] = 0
        self.matrix[7,2] = 1
        self.matrix[7,3] = 1
        self.matrix[7,4] = 1
        self.matrix[7,5] = 1
        self.matrix[7,6] = 0
        self.matrix[7,7] = 0
        self.matrix.show()
        return