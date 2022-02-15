import pygame as pg

pg.init()
screen = pg.display.set_mode([800, 600])

print('TASK: Show a green dot. ')

running = True
GREEN = (0, 255, 0)
radius = 50
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.draw.circle(screen, GREEN, (100, 100), radius)
    pg.display.update()

pg.quit()
