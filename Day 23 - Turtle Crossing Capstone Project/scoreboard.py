import turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.up()
        self.goto(-290, 250)
        self.write(f"Level: {self.score +1} ", move=False, align='left', font=FONT)

    def point(self):
        self.score += 1
        self.clear()
        self.write(f"Level: {self.score +1} ", move=False, align='left', font=FONT)

    def gameover(self):
        self.home()
        self.write("GAME OVER", move=False, align='center', font=FONT)