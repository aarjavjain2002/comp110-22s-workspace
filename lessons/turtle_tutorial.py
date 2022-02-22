"""A tutorial for turtle"""

import turtle
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()
import math


leo.goto(0,0)
leo.speed(5)
# leo.pencolor("red")
# leo.fillcolor('blue')
leo.fillcolor("green")
leo.hideturtle()

# leo.begin_fill()
# i: int = 0
# while i < 4:
#     leo.color("light blue")
#     leo.forward(300)
#     leo.left(120)
#     i += 1
# leo.end_fill()

leo.penup()
leo.goto(0, -(3**0.5)*50)
leo.pendown()


leo.forward(200)
leo.left(120)
leo.forward(400)
leo.left(120)
leo.forward(400)
leo.left(120)
leo.forward(200)



bob: Turtle = Turtle()
bob.color("red")
bob.hideturtle()
bob.speed(50)

bob.penup()
bob.goto(0, (-3**0.5)*50)
bob.pendown()

# side_length = 400
# i: int = 0
# while i<60:
#     bob.forward(side_length)
#     bob.left(120)
#     i += 1
#     side_length *= 0.97



done()