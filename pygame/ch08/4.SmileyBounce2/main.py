import pygame as pg

pg.init()
screen = pg.display.set_mode([800, 600])

print('TASK: All four walls can bounce smiley faces. ')

running = True
pic = pg.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pg.time.Clock()
speedx = 5
speedy = 5
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))
    picx += speedx
    picy += speedy

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx
    if picy <= 0 or picy + pic.get_height() >= 600:
        speedy = -speedy
    pg.display.update()
    timer.tick(60)

pg.quit()
