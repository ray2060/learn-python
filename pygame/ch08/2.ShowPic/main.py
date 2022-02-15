import pygame as pg

pg.init()
screen = pg.display.set_mode([800, 600])

print('TASK: Show the picture. ')
\
running = True
pic = pg.image.load("CrazySmile.bmp")
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(pic, (100, 100))
    pg.display.update()

pg.quit()
