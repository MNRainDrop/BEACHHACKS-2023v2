from settings import *
import pygame as p
from ball import ball

class player():
    def __init__(self) -> None:
        self.width = 100
        self.height = 10
        self.x = screenSize//2 - self.width//2
        self.y = screenSize - 100
        self.middlex = self.x + self.width//2
        self.middley = self.y + self.height//2

        #player movement
        self.speed = 8
        self.ball = None

        self.hasBall = True

    # action related functions
    def moveLeft(self):
        if self.x > 0:
            self.x -= self.speed
        else:
            self.x = 0

    def moveRight(self):
        if self.x < 800-self.width:
            self.x += self.speed        
        else:
            self.x = 800-self.width

    def shootBall(self, pos):
        if self.hasBall:
            self.hasBall = False
            self.ball = ball(self.middlex, self.middley, pos)
    
    def collideBall(self):
        if not self.hasBall:
            if self.x <= self.ball.x and self.x + self.width >= self.ball.x:
                if self.ball.y >= self.y:
                    self.ball.speedy *= -1

    # display related functions
    def display(self, screen, pos):
        p.draw.rect(screen, p.Color("#ffffff"), p.Rect(self.x, self.y, self.width, self.height))
        self.drawShot(screen, pos)
        if not self.hasBall:
            self.ball.draw(screen)
    

    def update(self):
        self.middlex = self.x + self.width//2
        self.middley = self.y + self.height//2
        if not self.hasBall:
            self.ball.update()
            self.collideBall()

    def drawShot(self, screen, pos):
        if self.hasBall:
            p.draw.line(screen, p.Color("#FFFFFF"), (self.middlex, self.middley), pos)

    