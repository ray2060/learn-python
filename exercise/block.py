from turtle import *
import time


class Block(Turtle):

    def __init__(self, size):
        self.size = size
        Turtle.__init__(self, shape='square', visible=False)
        self.pu()
        self.shapesize(size, 1, 0)
        self.fillcolor('black')
        self.st()

    def glow(self):
        self.fillcolor('red')

    def unglow(self):
        self.fillcolor('black')

    def __repr__(self):
        return 'Block size: {0}'.format(self.size)


if __name__ == '__main__':
    b = Block(10)
    b.setpos(0, 0)
    time.sleep(5)
    b.glow()
    time.sleep(3)
    b.unglow()
