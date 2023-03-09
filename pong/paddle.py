from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.penup()
        self.color('white')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def go_up(self):
        ''' for the paddle to move up'''
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        ''' for the paddle to move down'''
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)


