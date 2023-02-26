import pygame as p

class block():
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.width = self.height = 50

    def display(self, screen):
        p.draw.rect(screen, p.Color("#ffffff"), p.Rect((self.x * 100) + 25, (self.y * 100) + 50, self.width, self.height))
        