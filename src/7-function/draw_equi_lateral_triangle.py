import turtle
turtle.speed(10)
turtle.color('red')


def draw_equi_lateral_triangle(side):
    for i in range(3):
        turtle.forward(side)
        turtle.left(120)




draw_equi_lateral_triangle(100)

turtle.exitonclick()

