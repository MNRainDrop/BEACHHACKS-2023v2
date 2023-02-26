from settings import *
from player import player
from block import block

class blockbreaker:
    def __init__(self) -> None:
        self.player = player()
        self.rows = 1
        self.cols = 1
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

    def display(self, screen, pos):
        screen.fill("black")
        self.player.display(screen, pos)
        for block in self.blocks:
            block.display(screen)
        
    def blockCollision(self):
        if not self.player.hasBall:
            for block in self.blocks:
                if block.x < self.player.ball.x and block.x + block.width > self.player.ball.x:
                    # if block.y