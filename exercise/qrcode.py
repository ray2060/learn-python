import turtle as t

RADIUS = 15

length = int(input('请输入二维码大小：'))
lst1 = []
for i in range(length):
    lst1.append(list(input('请输入二维码的第%d行：' % (i + 1,))))

t.speed(8)
t.pensize(RADIUS)
t.penup()
t.goto(-RADIUS * (length - 1), RADIUS * (length + 1))
for i in range(length):
    for j in range(length):
        if int(lst1[i][j]) == 0:
            t.pendown()
            t.dot()
            t.penup()
        t.forward(RADIUS * 2)
    t.goto(-RADIUS * (length - 1), t.ycor() - RADIUS * 2)

t.hideturtle()
t.done()
