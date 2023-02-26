import pygame as p
from settings import *

def main():
    #initialize pygame
    p.init()
    screen = p.display.set_mode((screenSize, screenSize))


    clock = p.time.Clock()
    running = True
    while running:
        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type == p.MOUSEBUTTONDOWN:
                pos = p.mouse.get_pos()
            elif e.type == p.MOUSEBUTTONUP:
                pos = p.mouse.get_pos()
            elif e.type == p.KEYDOWN:
                if e.key == p.K_d:
                    pass
                if e.key == p.K_a:
                    pass
        clock.tick(maxFPS)
        p.display.flip()

if __name__ == "__main__":
    main()
