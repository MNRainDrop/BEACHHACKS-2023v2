from settings import *

class player:
    def __init__(self) -> None:
        self.width = 100
        self.height = 10
        self.x = screenSize//2 - self.width//2
        self.y = screenSize - 100

    
        