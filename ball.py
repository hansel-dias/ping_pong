# from time import sleep
from turtle import Turtle


class Ball(Turtle):
       def __init__(self):
              super().__init__()
              self.shape("circle")
              self.color("white")
              self.shapesize(stretch_wid=0.5,stretch_len=0.5)
              self.penup()
              self.x_position = 10
              self.y_position = 10

       def move_ball(self):
              new_x = self.xcor() + self.x_position
              new_y = self.ycor() + self.y_position
              self.goto((new_x, new_y))


       def ball_bounce_wall(self):
              # if self.ycor() > 280:
                     self.y_position *= -1

       def ball_bounce_paddle(self):
              # if self.ycor() > 280:
                     self.x_position *= -1

       def reset_position_x(self):
              self.goto(0,0)
              self.ball_bounce_paddle()

       def reset_position_y(self):
              self.goto(0,0)
              self.ball_bounce_wall()




