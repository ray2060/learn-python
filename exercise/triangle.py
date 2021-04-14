import turtle as t


def init(speed=6, pencolor='black', pensize=1, bgcolor='white', heading=270, fill=False, \
         fillcolor='red'):
    t.speed(speed)
    t.pencolor(pencolor)
    t.pensize(pensize)
    t.bgcolor(bgcolor)
    t.setheading(heading)
    t.fillcolor(fillcolor)
    global bool_fill
    bool_fill = fill

def triangle(side=200):
    for i in range(3):
        t.fd(side)
        t.rt(120)

init(speed=9)
for i in range(90):
    if bool_fill:
        t.begin_fill()
    triangle(200)
    t.rt(4)
    if bool_fill:
        t.end_fill()
t.hideturtle()
t.done()
