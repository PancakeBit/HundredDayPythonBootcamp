import turtle

timmy = turtle.Turtle()
screen = turtle.Screen()

def move_forward():
    timmy.forward(20)

def move_backward():
    timmy.backward(20)

def turn_left():
    timmy.left(20)

def turn_right():
    timmy.right(20)
def clearscreen():
    timmy.clear()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(turn_right, "d")
screen.onkey(turn_left, "a")
screen.onkey(move_backward, "s")
screen.onkey(clearscreen, "c")

screen.exitonclick()