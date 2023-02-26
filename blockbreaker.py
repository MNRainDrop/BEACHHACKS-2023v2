from settings import *
from player import player
from block import block
from ball import ball

class blockbreaker:
    def __init__(self) -> None:
        self.player = player()
        self.ball = ball()
        self.blocks = list()

    def update(self):
        #player
        self.player.update()

    def display(self, screen):
        screen.fill("black")
        self.player.display(screen)
        