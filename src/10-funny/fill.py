import turtle

turtle.color('red', 'blue')
turtle.speed(183848)
turtle.penup()
turtle.right(90)
turtle.forward(50)
turtle.left(90)
turtle.pendown()

turtle.begin_fill()
for i in range(3):
    turtle.forward(400)
    turtle.left(120)

turtle.end_fill()

turtle.done()