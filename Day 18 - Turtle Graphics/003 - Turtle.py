import turtle
from turtle import Turtle, Screen, colormode
import random

timmy = Turtle()
screen = Screen()
timmy.shape("turtle")
timmy.color("red")

palette = [(78, 198, 217), (107, 104, 236), (105, 233, 116), (231, 60, 58), (161, 231, 172), (90, 202, 116)]

def randomcolor():
    """Generate random color for use with turtle pencolor"""
    R = random.randint(0, 255)
    G = random.randint(0, 255)
    B = random.randint(0, 255)
    color = (R, G, B)
    return color


# -----------Draw a Square with Turtle---------------
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

# ------------- Draw dotted line --------------
def dottedLine():
    WIDTH = screen.window_width()
    HEIGHT = screen.window_height()

    for i in range(150):
        timmy.forward(10)
        timmy.up()
        x, y = timmy.pos()

        if x > WIDTH / 2:
            timmy.right(35)
        if x < -WIDTH / 2:
            timmy.right(56)
        if y > HEIGHT / 2:
            timmy.right(23)
        if y < -HEIGHT / 2:
            timmy.right(54)

        timmy.forward(10)
        timmy.down()


# Draw all polygons starting from triangle
def drawShapes():
    colormode(255)
    timmy.up()
    timmy.sety(200)
    timmy.setx(-50)
    timmy.down()
    for i in range(3, 11):
        angle = 360 / i
        timmy.color(randomcolor())
        for _ in range(i):
            timmy.forward(100)
            timmy.right(angle)

# Initiate Random Walk
def randomWalk():
    timmy.hideturtle()
    colormode(255)
    timmy.speed(10)
    timmy.pensize(8)

    for i in range(100):
        timmy.pencolor(randomcolor())
        turn = 90 * random.randint(0, 4)
        timmy.seth(turn)
        timmy.forward(20)


def drawCircle():
    colormode(255)
    timmy.speed('fastest')
    for i in range(100):
        timmy.pencolor(randomcolor())
        timmy.circle(100,)
        timmy.right(10)

def hirstpainting():
    """Exercise calls for use of the colorgram package, I have installed this package and ran it in main
    to get the palette variable"""
    # Full colorgram code
    # colors = colorgram.extract('image.jpg', 6)
    # palette = []
    # for i in colors:
    #     currentcolor = (i.rgb.r, i.rgb.g, i.rgb.b)
    #     palette.append(currentcolor)
    # print(palette)

    # ok ok ok ok, so this code is very cobbled together
    # i wanted to make something that works on any screen size but i'm sick at the moment
    # and confused about the math of it
    # i got it to sort of work? but it's not very good
    colormode(255)
    timmy.speed(0)
    timmy.pensize(10)
    height = screen.window_height()
    width = screen.window_width()
    timmy.penup()
    # go to lower left
    timmy.goto((-height / 2), (-width/2))
    size = 20

    for i in range(int(height/(size*2)) + 1):
        timmy.goto((-width / 2), timmy.ycor() + size * 2)
        for i in range(int(width/(size*3)) +1):
            timmy.color(random.choice(palette))
            timmy.forward(size * 3)
            timmy.dot(size)
# vvvvvvvvvvvvvv Call function below
hirstpainting()
# ^^^^^^^^^^^^^^ Call function above
screen.exitonclick()
