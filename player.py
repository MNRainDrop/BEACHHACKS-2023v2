from settings import *
import pygame as p

class player():
    def __init__(self) -> None:
        self.width = 100
        self.height = 10
        self.x = screenSize//2 - self.width//2
        self.y = screenSize - 100

        #player movement
        self.speed = 5


    def display(self, screen):
        p.draw.rect(screen, p.Color("#ffffff"), p.Rect(self.x, self.y, self.width, self.height))
        p.display.flip()
    
    def moveLeft(self):
        self.x -= self.speed

    def moveRight(self):
        self.x += self.speed        