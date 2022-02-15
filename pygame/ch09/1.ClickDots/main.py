import pygame as pg

pg.init()
screen = pg.display.set_mode([800, 600])

print('TASDK: Click to draw. ')

pg.display.set_caption("Click to draw")
running = True
RED = (255, 0, 0)
radius = 15

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            spot = event.pos
            pg.draw.circle(screen, RED, spot, radius)
    pg.display.update()

pg.quit()
