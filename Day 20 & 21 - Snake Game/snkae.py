import turtle
class Snake:
    def __init__(self, segments=3):
        '''Initialize Snake object, segments = number of starting segments'''
        self.segments = segments
        self.snake = []
        for i in range(self.segments):
            part = turtle.Turtle('square')
            part.up()
            part.color('white')
            part.goto(-20 * i, 0)
            self.snake.append(part)
        self.head= self.snake[0]

    def move(self):
        '''smove the snake forward by one block'''
        for i in range(len(self.snake) - 1, 0, -1):
            next_segment = self.snake[i - 1].pos()
            self.snake[i].goto(next_segment)
        self.snake[0].forward(20)

    def eaten(self):
        '''oncet the snake has eaten a food'''
        part = turtle.Turtle('square')
        part.up()
        part.color('white')
        part.goto(self.snake[len(self.snake)-1].pos())
        self.snake.append(part)

    def up(self):
        if self.head.heading() != 270:
            self.head.seth(90)
    def down(self):
        if self.head.heading() != 90:
            self.head.seth(270)
    def left(self):
        if self.head.heading() != 0:
            self.head.seth(180)
    def right(self):
        if self.head.heading() != 180:
            self.head.seth(0)