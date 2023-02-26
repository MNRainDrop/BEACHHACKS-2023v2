from settings import *

class ball:
    def __init__(self, x, y, pos) -> None:
        self.radius = 5
        self.x = x
        self.y = y
        self.speed = 5
        self.direction = pos
    
    def update(self):
        self.x += self.direction[0]

        