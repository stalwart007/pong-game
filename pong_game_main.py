from turtle import Turtle,Screen
from pong_game_paddle import Paddle
from pong_game_ball import Ball
from pong_game_scoreboard import Scoreboard
import time
my_screen = Screen()
my_screen.setup(width=1200,height=620)
my_screen.bgcolor("black")
my_screen.tracer(0)
left_paddle = Paddle((-550,0),"green")
right_paddle = Paddle((550,0),"red")
ball = Ball()
scoreboard = Scoreboard()
divider = Turtle()
divider.color("white")
divider.penup()
divider.pensize(3)
divider.goto(0,300)
divider.setheading(270)
for i in range(0,10):
    divider.pendown()
    divider.forward(30)
    divider.penup()
    divider.forward(30)
my_screen.listen()
my_screen.onkey(left_paddle.moveup,"w")
my_screen.onkey(left_paddle.movedown,"s")
my_screen.onkey(right_paddle.moveup,"Up")
my_screen.onkey(right_paddle.movedown,"Down")

game_is_on = True

while(game_is_on):
    time.sleep(0.025)
    my_screen.update()
    ball.move()
    if(ball.ycor() >= 300 or ball.ycor() <= -300):
        ball.bounce_y()
    if(ball.distance(left_paddle) < 75 and ball.xcor() < -519 or ball.distance(right_paddle) < 75 and ball.xcor() > 519):
        ball.bounce_x()
    if(ball.distance(right_paddle) > 75 and ball.xcor() > 590):
        scoreboard.left_score += 1
        scoreboard.update_scoreboard()
        ball.reset_ball_position()
    if(ball.distance(left_paddle) > 75 and ball.xcor() < -590):
        scoreboard.right_score += 1
        scoreboard.update_scoreboard()
        ball.reset_ball_position()
my_screen.exitonclick()