import pygame as pg

pg.init()
screen = pg.display.set_mode([800, 600])

print('TASDK: Drag to draw. ')

pg.display.set_caption("Click and drag to draw")
running = True
RED = (255, 0, 0)
radius = 15
mousedown = False

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mousedown = True
        if event.type == pg.MOUSEBUTTONUP:
            mousedown = False
    if mousedown:
        spot = event.pos
        pg.draw.circle(screen, RED, spot, radius)
    pg.display.update()

pg.quit()
