import turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.left(90)
        self.up()
        self.goto(STARTING_POSITION)

    def moveforward(self):
        self.forward(MOVE_DISTANCE)

    def goback(self):
        self.goto(STARTING_POSITION)