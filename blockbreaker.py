from settings import *
from player import player
from block import block

class blockbreaker:
    def __init__(self) -> None:
        self.player = player()
        self.blocks = list()

    def update(self):
        #player
        self.player.update()

    def display(self, screen, pos):
        screen.fill("black")
        self.player.display(screen, pos)
        