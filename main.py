import pygame as p
from settings import *
from blockbreaker import blockbreaker

def main():
    #initialize pygame
    p.init()
    screen = p.display.set_mode((screenSize, screenSize))
    bb = blockbreaker()
    clock = p.time.Clock()
    running = True
    while running:
        pos = p.mouse.get_pos()

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            elif e.type ==p.MOUSEBUTTONDOWN:
                bb.player.shootBall(pos)
                

        keys = p.key.get_pressed()
        if keys[p.K_a]:
            bb.player.moveLeft()
        if keys[p.K_d]:
            bb.player.moveRight()

        bb.update()
        bb.display(screen, pos)

        clock.tick(maxFPS)
        p.display.flip()

if __name__ == "__main__":
    main()
