# moving pong class
# paddle class
# score class

HEIGHT = 600
WIDTH = 800


from turtle import Turtle, Screen
from paddle_me import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(height=HEIGHT, width=WIDTH)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)



paddy_r = Paddle((350,0))
paddy_l = Paddle((-350,0))
ball = Ball()



screen.listen()   
screen.onkey(paddy_r.go_up,"Up")
screen.onkey(paddy_r.go_down,"Down")
screen.onkey(paddy_l.go_up,"w")
screen.onkey(paddy_l.go_down,"s")

game_is_on = True
while game_is_on:
       time.sleep(0.1)
       screen.update()        # screen refresh

       # Detect collision with wall
       if ball.ycor() > 280 or ball.ycor() < -280:
              ball.ball_bounce_wall()

       # Detect collision with paddle_r

       if ball.distance(paddy_r) < 50 and ball.xcor() > 320 or ball.distance(paddy_l) < 50 and ball.xcor() < -320:
              ball.ball_bounce_paddle()
       

       if ball.xcor() > 380:
              ball.reset_position_x()


       if ball.xcor() < -380:
              ball.reset_position_y()



       ball.move_ball()











































screen.exitonclick()