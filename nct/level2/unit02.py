import turtle as t


def init(speed, color):
    t.hideturtle()
    t.speed(speed)
    t.pencolor(color)

def draw(side):
    t.fd(side)
    t.left(120)

init(8, 'red')
for i in range(3):
    draw(100)
t.done()
