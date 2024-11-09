import turtle as t
from random import randint

def drawTree(depth):
	if depth == 8:
		return

	red = (8 - depth) * 18
	green = 192 - red
	blue = (8 - depth) * 9
	t.pencolor(red, green, blue)
	fd = 60
	x = 16 + depth * 0.5
	t.width(6 - (depth / 2))
	t.down()
	t.forward(fd)
	t.left(x)
	drawTree(depth + 1)
	t.right(2 * x)
	drawTree(depth + 1)
	t.left(x)
	t.up()
	t.backward(fd)

if __name__ == '__main__':
	screen = t.Screen()
	screen.colormode(255)
	t.up()
	t.setheading(90)
	t.goto(0, -200)
	t.speed(0)
	drawTree(0)
	t.hideturtle()
	t.done()