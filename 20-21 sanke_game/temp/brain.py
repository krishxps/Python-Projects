from turtle import Turtle
from random import randint as r

STARTING_POSI = [(0,0) , (-20,0) , (-40,0)]
MOVE_DISTANCE = 20


class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
       
    def create_snake(self):
        for position in STARTING_POSI:
            self.increase_length(position)
    
    def increase_length(self,position):
        new_segment = Turtle(shape="square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)
        
    
            
    def extend(self):
        self.increase_length(self.segments[-1].position())    
        
    def move(self):
        for seg_num in range(len(self.segments) - 1 ,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        
        self.head.forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
     
class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        
    def refresh(self):
        rand_x = r(-270,270)
        rand_y = r(-270,270)
        self.goto(x=rand_x , y=rand_y)
        
        
class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.width(4)
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score_inc()
        
    def score_inc(self):
        self.clear()
        self.write(f"Score : {self.score}", move=False, align='center', font='Arial')
        self.score += 1

    def game_over(self):
        self.width(6)
        self.goto(0,0)
        self.write("Game Over", move=False, align='center', font='Arial')