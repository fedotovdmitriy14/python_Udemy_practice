from turtle import Turtle, Screen

turtle = Turtle()
turtle.shape('turtle')
turtle.color('red')

# for _ in range(4):
#     turtle.forward(100)
#     turtle.left(90)

# for _ in range(15):
#     turtle.forward(10)
#     turtle.penup()
#     turtle.forward(10)
#     turtle.pendown()

number = 3
for _ in range(8):
    degrees = 360 / number
    for _ in range(number):
        turtle.forward(100)
        turtle.right(degrees)
    number += 1







screen = Screen()
screen.exitonclick()