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

Eye Positions
[0,1,2,3,4] 0
[0,1,2,3,4] 1
[0,1,2,3,4] 2
[0,1,2,3,4] 3
[0,1,2,3,4] 4

'''
from adafruit_ht16k33 import matrix

class Eyes:
    def __init__(self, i2c, brightness=7):
        self.matrix = matrix.Matrix8x8(i2c)
        self.Brightness(brightness)
    
    def Brightness(self, brightness):
        '''
        Define the brightness
        '''
        self.matrix.brightness = brightness
        return

    def Shutdown(self):
        '''
        Turn Off Display
        '''
        self.matrix.fill(0)
        return

    def Pos0_0(self):
        '''
        Looking Left
        '''
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
        self.matrix[1,2] = 0
        self.matrix[1,3] = 0
        self.matrix[1,4] = 1
        self.matrix[1,5] = 1
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 0
        self.matrix[2,3] = 0
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
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos0_1(self):
        '''
        Looking Center
        '''
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
        self.matrix[1,3] = 0
        self.matrix[1,4] = 0
        self.matrix[1,5] = 1
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 1
        self.matrix[2,3] = 0
        self.matrix[2,4] = 0
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
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos0_2(self):
        '''
        Looking Right
        '''
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
        self.matrix[1,4] = 0
        self.matrix[1,5] = 0
        self.matrix[1,6] = 1
        self.matrix[1,7] = 0
        # row 2
        self.matrix[2,0] = 1
        self.matrix[2,1] = 1
        self.matrix[2,2] = 1
        self.matrix[2,3] = 1
        self.matrix[2,4] = 0
        self.matrix[2,5] = 0
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
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos1_0(self):
        '''
        Looking Left
        '''
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
        self.matrix[2,1] = 0
        self.matrix[2,2] = 0
        self.matrix[2,3] = 1
        self.matrix[2,4] = 1
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 0
        self.matrix[3,2] = 0
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
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos1_1(self):
        '''
        Looking Transition Left
        '''
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
        self.matrix[2,2] = 0
        self.matrix[2,3] = 0
        self.matrix[2,4] = 1
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 0
        self.matrix[3,3] = 0
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
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos1_2(self):
        '''
        Looking Straight
        '''
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
        self.matrix[2,3] = 0
        self.matrix[2,4] = 0
        self.matrix[2,5] = 1
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 0
        self.matrix[3,4] = 0
        self.matrix[3,5] = 1
        self.matrix[3,6] = 1
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 1
        self.matrix[4,2] = 1
        self.matrix[4,3] = 1
        self.matrix[4,4] = 1
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos1_3(self):
        '''
        Looking Transition Right
        '''
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
        self.matrix[2,4] = 0
        self.matrix[2,5] = 0
        self.matrix[2,6] = 1
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 1
        self.matrix[3,4] = 0
        self.matrix[3,5] = 0
        self.matrix[3,6] = 1
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 1
        self.matrix[4,2] = 1
        self.matrix[4,3] = 1
        self.matrix[4,4] = 1
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos1_4(self):
        '''
        Looking Right
        '''
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
        self.matrix[2,5] = 0
        self.matrix[2,6] = 0
        self.matrix[2,7] = 1
        # row 3
        self.matrix[3,0] = 1
        self.matrix[3,1] = 1
        self.matrix[3,2] = 1
        self.matrix[3,3] = 1
        self.matrix[3,4] = 1
        self.matrix[3,5] = 0
        self.matrix[3,6] = 0
        self.matrix[3,7] = 1
        # row 4
        self.matrix[4,0] = 1
        self.matrix[4,1] = 1
        self.matrix[4,2] = 1
        self.matrix[4,3] = 1
        self.matrix[4,4] = 1
        self.matrix[4,5] = 1
        self.matrix[4,6] = 1
        self.matrix[4,7] = 1
        # row 5
        self.matrix[5,0] = 1
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos2_0(self):
        '''
        Looking Left
        '''
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
        self.matrix[3,1] = 0
        self.matrix[3,2] = 0
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
        self.matrix[5,1] = 1
        self.matrix[5,2] = 1
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

    def Pos2_1(self):
        '''
        Looking Transition Left
        '''
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
        self.matrix[3,2] = 0
        self.matrix[3,3] = 0
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
        self.matrix[5,2] = 1
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

    def Pos2_2(self):
        '''
        Looking Straight
        '''
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
        self.matrix[3,3] = 0
        self.matrix[3,4] = 0
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

    def Pos2_3(self):
        '''
        Looking Transition Right
        '''
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
        self.matrix[3,4] = 0
        self.matrix[3,5] = 0
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

    def Pos2_4(self):
        '''
        Looking Right
        '''
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
        self.matrix[3,5] = 0
        self.matrix[3,6] = 0
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

    def Pos3_0(self):
        '''
        Looking Left
        '''
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

    def Pos3_1(self):
        '''
        Looking Transition Left
        '''
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

    def Pos3_2(self):
        '''
        Looking Straight
        '''
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

    def Pos3_3(self):
        '''
        Looking Transition Right
        '''
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

    def Pos3_4(self):
        '''
        Looking Right
        '''
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

    def Pos4_0(self):
        '''
        Looking Left
        '''
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
        self.matrix[6,2] = 0
        self.matrix[6,3] = 0
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

    def Pos4_1(self):
        '''
        Looking Center
        '''
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
        self.matrix[6,3] = 0
        self.matrix[6,4] = 0
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

    def Pos4_2(self):
        '''
        Looking Right
        '''
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
        self.matrix[4,5] = 1
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
        self.matrix[6,4] = 0
        self.matrix[6,5] = 0
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
