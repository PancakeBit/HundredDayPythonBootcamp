from turtle import Turtle

# should have constants and variables for stuff like the placement of the write and the write parameters
# but for the purposes of this exercise, this code works and is easier to read

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.p1score = 0
        self.p2score = 0
        self.hideturtle()
        self.up()
        self.color('white')
        self.goto(0, 230)
        self.write(f"Score:\n  {self.p1score} | {self.p2score}", move=False, align='center', font=('Arial', 20, 'normal'))

    def addscore(self, xcor):
        self.clear()
        if xcor > 0:
            self.p2score +=1
        if xcor < 0:
            self.p1score +=1
        self.write(f"Score:\n  {self.p1score} | {self.p2score}", move=False, align='center', font=('Arial', 20, 'normal'))
