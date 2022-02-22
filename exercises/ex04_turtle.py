"""The Batman symbol drawn with Turtle - inspired by Chris Nolan's symbol and the upcoming Batman movie.

Additional tools I used included background color and circles.
I used the circles in a loop with varying radii per quadrant to draw multiple ellipses and filled them with the background color.
This gives the unique shape of the wings.
"""

__author__ = "730506302"

from turtle import bgcolor, Turtle, colormode, done
colormode(255)
bgcolor("maroon")


def main() -> None:
    """The primary function for the program."""
    turtle = Turtle()
    turtle.hideturtle()
    turtle.speed(0)

    # The question mark line
    question_mark(turtle)

    turtle.pensize(2)

    # The 3 main rectangles
    rectangle(turtle, 250, 100, -125, -50)
    rectangle(turtle, 320, 180, 125, -50)
    rectangle(turtle, 320, 180, -445, -50)

    # The ears
    triangle(turtle, 50, -75, 50, 0)
    triangle(turtle, 50, 25, 50, 0)

    # The tail
    triangle(turtle, 100, -50, -50, -60)

    # The circles for wings
    circle(turtle, 100, 135, 50)
    circle(turtle, 100, -135, 50)

    # Top ellipses for wings
    ellipse(turtle, 100, "maroon", 375, 30)
    ellipse(turtle, 100, "maroon", -525, 30)

    # Second ellipses for wings
    ellipse(turtle, 100, "maroon", 300, -75)
    ellipse(turtle, 100, "maroon", -437, -75,)

    # Extra circles for refinement
    turtle.speed(12)
    circle(turtle, 25, 430, -15)
    circle(turtle, 25, -443, -17)

    # The question mark
    circle2(turtle, 100, 0, 100)
    turtle.pensize(2)
    triangle(turtle, 50, 25, 50, 0)
    square(turtle, 30, -21.21, -180)
    done()


def rectangle(turtle: Turtle, length: float, breadth: float, x: float, y: float) -> None:
    """Creates a rectangle for a given length and breadth and given starting co ordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.seth(0)
    turtle.pendown()
    turtle.pencolor("black")
    turtle.fillcolor("black")
    i: int = 0
    while i < 2:
        turtle.begin_fill()
        turtle.forward(length)
        turtle.left(90)
        turtle.forward(breadth)
        turtle.left(90)
        i += 1
        turtle.end_fill()


def triangle(turtle: Turtle, side: float, x: float, y: float, h: float) -> None:
    """Creates a triangle with a given side length, given starting co ordinates, and direction."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.seth(h)
    turtle.color("black")
    turtle.begin_fill()
    i: int = 0
    while i < 3:
        turtle.forward(side)
        turtle.left(120)
        i += 1
    turtle.end_fill()


def ellipse(turtle: Turtle, radius: float, color: str, x: float, y: float) -> None:
    """Creates an ellipse with a given radius, given starting co ordinates, and with given color of ellipse."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.setheading(-45)    
    turtle.color(color)

    i: int = 0
    while i < 2:
        turtle.begin_fill()
        turtle.circle(radius, 90)
        turtle.circle(radius // 2, 90)
        turtle.end_fill()
        i += 1


def circle(turtle: Turtle, radius: float, x: float, y: float) -> None:
    """Creates a circle with given radius and given starting co ordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pencolor("maroon")
    turtle.fillcolor("maroon")
    turtle.seth(0)

    turtle.begin_fill()
    turtle.circle(radius, 360)
    turtle.end_fill()


def circle2(turtle: Turtle, radius: float, x: float, y: float) -> None:
    """Creates a circle with given radius and given starting co ordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.pensize(90)
    turtle.pencolor("darkgreen")
    turtle.seth(0)
    turtle.circle(radius, 270)


def question_mark(turtle: Turtle) -> None:
    """Creates a line part of the question mark."""
    turtle.pensize(90)
    turtle.penup()
    turtle.color("darkgreen")
    turtle.goto(0, 100)
    turtle.seth(-90)
    turtle.pendown()
    turtle.forward(160)


def square(turtle: Turtle, side: float, x: float, y: float) -> None:
    """Creates a square part of the question mark with a given side length and co ordinates."""
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.color("darkgreen")
    turtle.pensize(40)
    turtle.seth(-45)
    i: int = 0
    while i < 4:
        turtle.forward(side)
        turtle.left(90)
        i += 1
    

if __name__ == "__main__":
    main()