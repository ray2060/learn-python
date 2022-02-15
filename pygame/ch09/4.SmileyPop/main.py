import pygame as pg
import random as r


class Smiley(pg.sprite.Sprite):
    pos = (0,0)
    xvel = 1
    yvel = 1
    scale = 100

    
    def __init__(self, pos, xvel, yvel):
        pg.sprite.Sprite.__init__(self)
        self.image = pic
        self.scale = r.randrange(10,100)
        self.image = pg.transform.scale(self.image, (self.scale,self.scale))
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.x = pos[0] - self.scale/2
        self.rect.y = pos[1] - self.scale/2
        self.xvel = xvel
        self.yvel = yvel

    
    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        if self.rect.x <= 0 or self.rect.x > screen.get_width() - self.scale:
            self.xvel = -self.xvel
        if self.rect.y <= 0 or self.rect.y > screen.get_height() - self.scale:
            self.yvel = -self.yvel


BLACK = (0,0,0)
pg.init()
screen = pg.display.set_mode([800,600])
pg.display.set_caption("Pop a Smiley")
mousedown = False
keep_going = True
clock = pg.time.Clock()
pic = pg.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0,0))
pic.set_colorkey(colorkey)
sprite_list = pg.sprite.Group()

while keep_going:
    for event in pg.event.get(): 
        if event.type == pg.QUIT: 
            keep_going = False
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0]:
                mousedown = True
            elif pg.mouse.get_pressed()[2]:
                pos = pg.mouse.get_pos()
                clicked_smileys = [s for s in sprite_list if s.rect.collidepoint(pos)]
                sprite_list.remove(clicked_smileys)
        if event.type == pg.MOUSEBUTTONUP:
            mousedown = False
    screen.fill(BLACK)
    sprite_list.update()
    sprite_list.draw(screen)
    clock.tick(60)
    pg.display.update()
    if mousedown:
        speedx = r.randint(-5, 5)
        speedy = r.randint(-5, 5)
        newSmiley = Smiley(pg.mouse.get_pos(),speedx,speedy)
        sprite_list.add(newSmiley)
        
pg.quit()
