import turtle
import paddles
import ball
import scoreboard
from time import sleep

# --------------- IMPORTANT -----------------------#
# Controls are set to "W" and "S" for RIGHT player
#                 and "O" and "L" for LEFT player
# I have a 60% keyboard with FN needed for the arrow keys ok

# Very rough Pong game, Here are the problems and thinking solutions:
# 1. Ball only moves in set trajectory,
#   -  can modify by making angle of ball bounce depending on location of bounce
# 2. Slightly sluggish? Seems to be problem with the turtle module of python
#   -  Slightly fixed by halving sleep time, lowering sleep time
# 3. Controls are set to my keyboard because FN arrows
# 4. NO COMPUTER AI
#    -  Researched and found code for basic AI that attempts to reach the ball
#       Once it is going towards COMP, feels unfair, not very integrative to turtle
# 5. Hitting the ball directly with the TOP of the paddle causes logic to be true multiple times
#    and so the ball bounces multiple times across the paddle
#    -   can maybe set it to happen only once per few frames? but will bloat the code

# initialize screen
screen = turtle.Screen()
screen.setup(width=800,height=600)
screen.title("Pong from Turtle")
screen.bgcolor('black')
screen.tracer(0)

# paddles, ball, scoreboard
player1 = paddles.Paddle((350, 0))
player2 = paddles.Paddle((-350, 0))
ball = ball.Ball()
scoreboard = scoreboard.Scoreboard()

screen.listen()
#keypresses for player1
screen.onkeypress(fun=player1.moveup, key='w')
screen.onkeypress(player1.movedown, 's')

#keypresses for player2
screen.onkeypress(fun=player2.moveup, key='o')
screen.onkeypress(player2.movedown, 'l')

# no gameover state for this game, just play until you get tired and close it
# will add exit functionality
gamestart = True
while gamestart:
    sleep(0.05)
    ball.move()
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bouncewall()
    if (ball.distance(player1) < 50 and ball.xcor() > 330 ) or (ball.distance(player2) < 50 and ball.xcor() < -330) :
        ball.bouncepaddle()
    if ball.xcor() > 380 or ball.xcor() < -380:
        scoreboard.addscore(ball.xcor())
        ball.someonescored()
    screen.update()

screen.exitonclick()
