import turtle
import random

turtle.color("green")
turtle.speed(10)
def draw_square(side_length):
    for i in range(4):
        turtle.forward(side_length)
        turtle.left(90)


counter = 0
while counter < 90:
    rand_side = random.randint(100, 300)
    draw_square(rand_side)
    turtle.right(4)
    counter += 1

turtle.exitonclick()