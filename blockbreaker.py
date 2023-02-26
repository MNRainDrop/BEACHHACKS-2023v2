from settings import *
from player import player
from block import block

class blockbreaker:
    def __init__(self) -> None:
        self.player = player()
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

    def display(self, screen, pos):
        screen.fill("black")
        self.player.display(screen, pos)
        for block in self.blocks:
            block.display(screen)
        
    def blockCollision(self):
        if not self.player.hasBall:
            for block in self.blocks:
                remove = False
                if block.x < self.player.ball.x and block.x + block.width > self.player.ball.x:
                    if block.y+block.height > self.player.ball.y and block.y < self.player.ball.y:
                        self.player.ball.speedy = self.player.ball.speedy * -1
                        remove = True
                # if block.y < self.player.ball.y and block.y + block.height > self.player.ball.y:
                #     if block.x+block.width > self.player.ball.x and block.x < self.player.ball.x:
                #         self.player.ball.speedy = self.player.ball.speedy * -1
                #         self.player.ball.speedx = self.player.ball.speedx * -1
                #         remove = True
                if remove:
                    self.blocks.remove(block)
                    