import turtle
turtle.color('red', 'yellow')
turtle.speed(1000)
turtle.penup()
turtle.backward(400)
turtle.forward(1)
turtle.pendown()

turtle.begin_fill()
while True:
    turtle.forward(400)
    turtle.left(170)
    if abs(turtle.position()) < 1:
        break

turtle.end_fill()
turtle.done()