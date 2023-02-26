from settings import *
import pygame as p
from player import player
from block import block

class blockbreaker:
    def __init__(self) -> None:
        self.level = 1
        self.player = player(self.level)
        self.rows = 4
        self.cols = 8
        self.blocks = list()
        self.initBlocks()

    def initBlocks(self):
        for i in range(self.cols):
            for j in range(self.rows):
                self.blocks.append(block(i, j))

    def update(self):
        #player
        self.player.update()
        self.blockCollision()
        if len(self.blocks) == 0:
            self.levelUp()

    def levelUp(self):
        self.level += 1
        self.player = player(self.level)
        self.initBlocks()

    def display(self, screen, pos):
        screen.fill("pink")
        p.draw.line(screen, p.Color("black"), (screenSize, 0), (screenSize,screenSize))
        self.player.display(screen, pos)
        for block in self.blocks:
            block.display(screen)
        
    def blockCollision(self):
        if not self.player.hasBall:
            for block in self.blocks:
                remove = False
                #collides with top and bottom, only one working atm
                if block.x < self.player.ball.x and block.x + block.width > self.player.ball.x:
                    if abs(block.y+block.height - self.player.ball.y) < 5:
                        self.player.ball.speedy *= -1
                        remove = True
                    if abs(block.y - self.player.ball.y) < 5:
                        self.player.ball.speedy *= -1
                        remove = True
                #collides with sides, but shoots straight with bouncing
                if block.y < self.player.ball.y and block.y + block.height > self.player.ball.y:
                    if abs(block.x+block.width- self.player.ball.x) < 5:
                        self.player.ball.speedx *= -1
                        remove = True
                    if abs(block.x+ - self.player.ball.x) < 5:
                        self.player.ball.speedx *= -1
                        remove = True
                if remove:
                    self.blocks.remove(block)
                    