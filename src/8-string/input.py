import turtle
turtle.shape('turtle')
turtle.speed(10)
name = turtle.textinput('Name', 'What is your name?')
name = name.lower()
if name.startswith('mr'):
    print('Hello Sir, How are you?')
elif name.startswith('mrs') or name.startswith('miss') or name.startswith('ms'):
    print('Hello Madam, How are you?')
else:
    name = name.capitalize()
    str = 'Hi ' + name + '! How are you?'
    print(str)

turtle.exitonclick()