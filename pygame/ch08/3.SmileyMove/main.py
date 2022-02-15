import pygame as pg

pg.init()
screen = pg.display.set_mode([600, 600])

print('TASK: Let the smiley face move. ')

running = True
pic = pg.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.blit(pic, (picx, picy))
    picx += 1
    picy += 1
    pg.display.update()

pg.quit()
