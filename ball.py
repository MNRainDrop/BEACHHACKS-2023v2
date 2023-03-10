from settings import *
import pygame as p
from math import *

class ball:
    def __init__(self, x, y, pos, level) -> None:
        self.radius = 10
        self.x = x
        self.y = y
        self.speedx = 10 + (level-1)*1
        self.speedy = 10 + (level-1)*1
        self.theta = atan2(pos[1]-y, pos[0]-x)
    
    def update(self):
        # left wall and right wall
        if self.x < 0 or self.x > screenSize:
            self.speedx = self.speedx * -1
        # top wall
        if self.y < 0:
            self.speedy = self.speedy * -1
        # angle
        self.x += self.speedx * cos(self.theta)
        self.y += self.speedy * sin(self.theta)

    def draw(self, screen):
        p.draw.circle(screen, p.Color("white"), (self.x, self.y), self.radius)