from turtle import Turtle

# should have constants and variables for stuff like the placement of the write and the write parameters
# but for the purposes of this exercise, this code works and is easier to read

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open('highscore') as hs:
                self.highscore = int(hs.read())
        except:
            with open('highscore', 'w') as hs:
                hs.write('0')
            with open('highscore') as hs:
                self.highscore = int(hs.read())
        self.hideturtle()
        self.up()
        self.color('white')
        self.goto(0, 270)
        self.writescore()

    def writescore(self):
        self.clear()
        self.write(f"Score: {self.score} | High Score: {self.highscore}", move=False, align='center', font=('Arial', 20, 'normal'))

    def gameover(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.writescore()
        with open('highscore', 'w') as hs:
            hs.write(str(self.highscore))

    def addscore(self):
        self.score += 1
        self.writescore()