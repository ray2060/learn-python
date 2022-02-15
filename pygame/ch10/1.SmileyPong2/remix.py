import pygame as pg

pg.init()
screen = pg.display.set_mode([800, 600])

running = True
pic = pg.image.load("CrazySmile.bmp")
colorkey = pic.get_at((0, 0))
pic.set_colorkey(colorkey)
picx = 0
picy = 0
BLACK = (0, 0, 0)
timer = pg.time.Clock()
speedx = 10
speedy = 10
WHITE = (255, 255, 255)
pw = 200
ph = 25
px = 300
py = 550
picw = 100
pich = 100
points = 0
lives = 5000
font = pg.font.SysFont("Times", 24)

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_F1:
                points = 0
                lives = 5000
                picx = 0
                picy = 0
                speedx = 10
                speedy = 10
    
    picx += speedx
    picy += speedy
    speedx *= 1.005
    speedy *= 1.005

    if picx <= 0 or picx + pic.get_width() >= 800:
        speedx = -speedx * 2
    if picy <= 0:
        speedy = -speedy
    if picy >= 500:
        lives -= 1
        speedy = -5
        speedx = 5

    screen.fill(BLACK)
    screen.blit(pic, (picx, picy))

    px = pg.mouse.get_pos()[0]
    px -= pw / 2
    pg.draw.rect(screen, WHITE, (px, py, pw, ph))

    if picy + pich >= py and picy + pich <= py + ph and speedy >= 0:
        if picx + picw/ 2 >= px and picx + picw / 2 <= px + pw:
            points += 1
            speedy = -speedy * 2

    draw_string = f'Lives: {lives} Points: {points}'
    if lives < 1:
        speedx = speedy = 0
        draw_string = f"Game Over. Your score was: {points}. Press F1 to play again"
    text = font.render(draw_string, True, WHITE)
    text_rect = text.get_rect()
    text_rect.centerx = screen.get_rect().centerx
    text_rect.y = 10
    screen.blit(text, text_rect)
    pg.display.update()
    timer.tick(60)

pg.quit()
