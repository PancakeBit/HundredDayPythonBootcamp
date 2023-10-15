import turtle
import random

colors = ['red', 'blue', 'pink', 'green', 'orange', 'magenta', 'navy']

turtles = []

screen = turtle.Screen()
screen.setup(width=500, height=400)
height = screen.window_height()
width = screen.window_width()

i=0
for i in range(6):
    timmy = turtle.Turtle('turtle')
    timmy.up()
    timmy.speed(9)
    timmy.color(colors[i])
    turtles.append(timmy)
    i += 1

print(turtles)
i = 80
equaldistance = (height/2) / len(turtles)
for turtle in turtles:
    turtle.goto(-230, i)
    i -= 30

def racebegin():
    global turtles
    gameover = False
    while gameover == False:
        for turtle in turtles:
            turtle.forward(random.randint(0,10))
            if turtle.xcor() >= (width/2) -20:
                gameover = True
                break

#bet = screen.textinput("Place Bet", "Who do you think will win the race?")
screen.listen()
screen.onkey(fun=racebegin, key='space')

screen.exitonclick()