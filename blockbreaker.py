from settings import *
from player import player
from block import block

class blockbreaker:
    def __init__(self) -> None:
        self.player = player()
        self.rows = 4
        self.cols = 8
        self.blocks = [[block(i, j) for j in range(self.rows)] for i in range(self.cols)]

    def update(self):
        #player
        self.player.update()
        self.blockCollision()

    def display(self, screen, pos):
        screen.fill("black")
        self.player.display(screen, pos)
        for i in range(self.cols):
            for j in range(self.rows):
                self.blocks[i][j].display(screen)
        
    def blockCollision(self):
        if not self.player.hasBall:
            for i in range(self.cols):
                for j in range(self.rows):
                    block = self.blocks[i][j]
                    if block.x <= self.player.ball.x and block.x + block.width >= self.player.ball.x:
                        if self.player.ball.y >= block.y:
                            self.player.ball.speedx = self.player.ball.speedx * -1
                        if self.player.ball.y <= block.y + block.height:
                            self.player.ball.speedx = self.player.ball.speedx * -1
                    if block.y <= self.player.ball.y and block.y + block.height >= self.player.ball.y:
                        if self.player.ball.x >= block.x:
                            self.player.ball.speedy = self.player.ball.speedy * -1
                        if self.player.ball.x <= block.x + block.width:
                            self.player.ball.speedy = self.player.ball.speedy * -1
                    
