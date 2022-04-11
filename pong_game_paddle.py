from turtle import Turtle

paddles = []

class Paddle(Turtle):
    def __init__(self,pos,_color):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=7.5,stretch_len=1.5)
        self.color(_color)
        self.penup()
        self.goto(pos)
        paddles.append(self)
        
    def moveup(self):
        if(self.ycor() <= 230):
            self.goto(self.xcor(),self.ycor()+40)
    def movedown(self):
        if(self.ycor() >= -230):
            self.goto(self.xcor(),self.ycor()-40)
