from settings import *
import pygame as p
from math import *

class ball:
    def __init__(self, x, y, pos) -> None:
        self.radius = 5
        self.x = x
        self.y = y
        self.speedx = 10
        self.speedy = 10
        self.theta = atan2(pos[1]-y, pos[0]-x)
    
    def update(self):
        if self.x < 0 or self.x > 800:
            self.speedx = self.speedx * -1
        if self.y < 0:
            self.speedy = self.speedy * -1
        self.x += self.speedx * cos(self.theta)
        self.y += self.speedy * sin(self.theta)

    def draw(self, screen):
        p.draw.circle(screen, p.Color("red"), (self.x, self.y), self.radius)