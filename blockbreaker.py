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

    def display(self, screen, pos):
        screen.fill("black")
        self.player.display(screen, pos)
        for i in range(self.cols):
            for j in range(self.rows):
                self.blocks[i][j].display(screen)
        