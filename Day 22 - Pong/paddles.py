import turtle


class Paddle(turtle.Turtle):
    def __init__(self, xy):
        super().__init__()
        self.xy = xy
        self.shape('square')
        self.up()
        self.color('white')
        self.goto(xy)
        self.shapesize(5, 1, 2)
        self.speed(0)

    def moveup(self):
        self.goto(self.xcor(), self.ycor()+10)
    def movedown(self):
        self.goto(self.xcor(), self.ycor()-10)