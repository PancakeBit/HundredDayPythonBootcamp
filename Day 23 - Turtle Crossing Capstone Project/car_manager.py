import turtle
from random import randint

# made starting move distance into 2 from 5 so that level "1" is just a walk forward
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 2
MOVE_INCREMENT = 10

class CarManager(turtle.Turtle):
    def __init__(self, score):
        super().__init__()
        self.up()
        self.score = score
        self.speed(0)
        self.shape('square')
        self.move_distance = STARTING_MOVE_DISTANCE
        self.reinit()
        self.increasespeed(score)
        self.backtoright()

    def move(self):
        newx = self.xcor() - self.move_distance
        self.goto(newx, self.ycor())
        if self.xcor() < -300:
            self.backtoright()

    def increasespeed(self, score):
        self.move_distance = (MOVE_INCREMENT * score) + STARTING_MOVE_DISTANCE

    def backtoright(self):
        randY = randint(-230, 230)
        self.reinit()
        self.goto(300, randY)

    def reinit(self):
        self.color(COLORS[randint(0,len(COLORS)-1)])
        self.size = randint(1,4)
        self.shapesize(1, self.size)
