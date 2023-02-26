import pygame as p
from settings import *
from blockbreaker import blockbreaker

def main():
    #initialize pygame4
    
    p.init()
    screen = p.display.set_mode((screenSize + 200, screenSize))
    bb = blockbreaker()
    clock = p.time.Clock()

    #initialize pictures
    images.append(p.transform.scale(p.image.load("assets/heart.png"), (100, 100)))

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
        if keys[p.K_r]:
            bb = blockbreaker()
        if keys[p.K_ESCAPE]:
            running = False
        if bb.player.lives <= 0:
            running = False

        bb.update()
        bb.display(screen, pos)

        clock.tick(maxFPS)
        p.display.flip()

if __name__ == "__main__":
    main()
