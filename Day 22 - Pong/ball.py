import turtle


class Ball(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.up()
        self.color('white')
        self.ydirection = -5
        self.xdirection = 5
        self.move()

    def move(self):
        newx = self.xcor() + self.xdirection
        newy = self.ycor() + self.ydirection
        self.goto(newx, newy)
    def increasespeed(self):
        self.ydirection = self.ydirection * 1.2
        self.xdirection = self.xdirection * 1.2

    def bouncewall(self):
        self.ydirection = self.ydirection * -1
        #newy = self.ycor() + self.ydirection
        #self.goto(self.xcor(), newy)

    def bouncepaddle(self):
        self.xdirection = self.xdirection * -1
        self.increasespeed()
        #newx = self.xcor() + self.xdirection
        #self.goto(newx, self.ycor())

    def resetspeed(self):
        if self.xdirection > 0:
            self.xdirection = 5
        elif self.xdirection < 0:
            self.xdirection = -5
        if self.ydirection > 0:
            self.ydirection = 5
        elif self.ydirection < 0:
            self.ydirection = -5
    def someonescored(self):
        self.home()
        self.xdirection = self.xdirection *-1
        self.resetspeed()
