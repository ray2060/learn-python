'''
import random

user_input1 = int(input())
user_input2 = int(input())

lst = []
if user_input1 < user_input2:
    for i in range(user_input1, user_input2+1):
        lst.append(i)
    num1 = random.choice(lst)
elif user_input1 > user_input2:
    for i in range(user_input2, user_input1+1):
        lst.append(i)
    num1 = random.choice(lst)
else:
    num1 = user_input1

num2 = bin(num1)

print('%d %s' % (num1, num2))


import random

x = int(input())
y = int(input())
if x > y:
    x, y = y, x
a = random.randint(x, y)
print(a, bin(a))
'''

# 巩固练习2
import turtle as t
import random


def draw(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()
    for i in range(5):
        t.fd(30)
        t.left(144)
    t.penup()
    
def get_pos():
    a = random.randint(-200, 200)
    return a

for i in range(10):
    draw(get_pos(), get_pos())

t.hideturtle()
t.done()
