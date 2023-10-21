# This is Frogger, lol

# Note to self: Need to think more with OOP in mind
# A lot of aspects here in this main code could have been done easier in an object

import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
screen.listen()

screen.onkey(fun=player.moveforward, key='space')

cars = []
loopcounter = 0
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    if len(cars) < 20:
        loopcounter +=1
        if loopcounter == 5:
            car = CarManager(score.score)
            cars.append(car)
            loopcounter = 0
    for car in cars:
        car.move()
    # Check if player is at the end, add one point, increase speed, then send them back
    if player.ycor() > 280:
        score.point()
        for car in cars:
            car.increasespeed(score.score)
        player.goback()
    # Check for player collision with any car object
    # jank as heck, played around with the numbers for collision and this works best?
    # For some reason the distance detection is late by about 5 units, hence +5
    # i.e. if I set it to stop at distance 30 it will stop at distance 25
    for car in cars:                     #absolute value of the 2 absolute values must be less than 15
        if player.distance(car) < (10*car.size) +5 and abs((abs(player.ycor()) - abs(car.ycor()))) < 15:
            game_is_on = False
score.gameover()
screen.exitonclick()
