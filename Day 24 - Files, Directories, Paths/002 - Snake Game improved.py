import turtle
from snkae import Snake
import food
import scoreboard
import time

# game has issue where negative X and positive Y look closer than they should be?
# left and top side reach collision before colliding with wall
# offset left and top side by 10 pixels for now

screen = turtle.Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game!!")
screen.bgcolor('black')

screen.tracer(n=0)
screen.update()

snake = Snake(5)

food = food.Food()
score = scoreboard.Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key='w')
screen.onkey(fun=snake.left, key='a')
screen.onkey(fun=snake.down, key='s')
screen.onkey(fun=snake.right, key='d')

# press space to grow snake, for debugging purposes
screen.onkey(fun=snake.eaten, key='space')

start = True
while start:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.eaten()
        score.addscore()
    # if snake collides with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -280:
        score.gameover()
        snake.gameover()
    # if snake collides with self
    for part in snake.snake[1:]:
        if snake.head.distance(part) < 15:
            score.gameover()
            snake.gameover()
    screen.update()

screen.exitonclick()