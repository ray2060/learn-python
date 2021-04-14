import turtle as t
import time
import random
import sys


t.speed(0)
t.bgcolor('black')
colors = {
    20:'green',
    40:'red',
    60:'yellow',
    80:'red',
    100:'blue',
    120:'green',
    140:'yellow'
    }
for i in range(20, 160, 20):
    t.pencolor(colors[i])
    for j in range(18):
        t.circle(i)
        t.left(20)
t.pencolor(1, 0.2, 1)
for i in range(10, 12):
    t.setpos(-1 * i, i)
    for j in range(60):
        t.forward(random.randint(20, 28))
        t.left(176)
        time.sleep(0.1)
t.hideturtle()
t.mainloop()
sys.exit()
