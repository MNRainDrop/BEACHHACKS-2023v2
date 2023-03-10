from settings import *
import pygame as p
from ball import ball

class player():
    def __init__(self, level) -> None:
        self.width = 100
        self.height = 10
        self.x = screenSize//2 - self.width//2
        self.y = screenSize - 100
        self.middlex = self.x + self.width//2
        self.middley = self.y + self.height//2

        #player movement
        self.speed = 8 + level
        self.ball = None
        self.lives = 3
        self.level = level
        self.hasBall = True

    # action related functions
    def moveLeft(self):
        if self.x > 0:
            self.x -= self.speed
        else:
            self.x = 0

    def moveRight(self):
        if self.x < screenSize-self.width:
            self.x += self.speed        
        else:
            self.x = screenSize-self.width

    def shootBall(self, pos):
        if self.hasBall:
            self.hasBall = False
            self.ball = ball(self.middlex, self.middley, pos, self.level)
    
    def collideBall(self):
        if not self.hasBall:
            if self.ball.y > self.y:
                if self.x <= self.ball.x and self.x + self.width >= self.ball.x:
                    self.ball.speedy *= -1
                else:
                    self.hasBall = True
                    self.lives -= 1

    # display related functions
    def display(self, screen, pos):
        p.draw.rect(screen, p.Color("#ffffff"), p.Rect(self.x, self.y, self.width, self.height))
        self.drawShot(screen, pos)
        if not self.hasBall:
            self.ball.draw(screen)
        self.displayLife(screen)
        
    def displayLife(self,screen):
        
        for i in range(self.lives):
            screen.blit(images[0], p.Rect(screenSize+50, (screenSize-150)-i*200, 100, 100))

    

    def update(self):
        self.middlex = self.x + self.width//2
        self.middley = self.y + self.height//2
        if not self.hasBall:
            self.ball.update()
            self.collideBall()

    def drawShot(self, screen, pos):
        if self.hasBall:
            p.draw.line(screen, p.Color("#FFFFFF"), (self.middlex, self.middley), pos)

    