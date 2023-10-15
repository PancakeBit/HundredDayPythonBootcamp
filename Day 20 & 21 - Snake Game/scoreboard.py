from turtle import Turtle

# should have constants and variables for stuff like the placement of the write and the write parameters
# but for the purposes of this exercise, this code works and is easier to read

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.color('white')
        self.goto(0, 270)
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))


    def gameover(self):
        self.home()
        self.color('red')
        self.write("GAME OVER", move=False, align='center', font=('Arial', 20, 'normal'))
    def addscore(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))
