import pygame as p
from settings import *

class block():
    def __init__(self, x, y) -> None:
        self.x = x*screenSize//8 + screenSize//32
        self.y = y*screenSize//8 + screenSize//32
        self.width = self.height = 50

    def display(self, screen):
        p.draw.rect(screen, p.Color("#ffffff"), p.Rect(self.x, self.y, self.width, self.height))
        