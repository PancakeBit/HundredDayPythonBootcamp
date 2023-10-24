from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.color('green')
        self.speed(0)
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)

        self.goto(randomX, randomY)
        self.refresh()

    def refresh(self):
        randomX = random.randint(-280, 280)
        randomY = random.randint(-280, 280)

        self.goto(randomX, randomY)

