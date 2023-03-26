import turtle
import random

turtle.speed(100)
turtle.penup()
color = ['red', 'green', 'blue', 'yellow', 'orange', 'black', 'purple']

for i in range(2000):
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    c = random.randint(0, len(color)-1)
    turtle.color(color[c])
    turtle.setposition(x, y)
    turtle.dot()

turtle.done()