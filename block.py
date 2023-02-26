import pygame as p
from settings import *

class block():
    def __init__(self, x, y) -> None:
        self.x = x*screenSize//8 + screenSize//32
        self.y = y*screenSize//8 + screenSize//32
        self.width = self.height = 50

    def display(self, screen):
        screen.blit(images[1], p.Rect(self.x, self.y, self.width, self.height))
        #p.draw.rect(screen, p.Color("white"), p.Rect(self.x, self.y, self.width, self.height))
        