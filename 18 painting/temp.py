import turtle as t
import random
t.colormode(255)
tim = t.Turtle()

color = [ (58, 106, 148), (224, 200, 110), (134, 84, 58), (223, 138, 62), (196, 145, 171)]
tim.penup()
tim.goto(-320, -300)
tim.pensize(20) 

def move():
    for _ in range(10):
        tim.color(random.choice(color))
        tim.pendown()
        tim.forward(1)
        tim.penup()
        tim.forward(69)

def left():
    tim.left(90)
    tim.forward(70)
    tim.left(90)
    tim.forward(70)

def right():
    tim.right(90)
    tim.forward(70)
    tim.right(90)
    tim.forward(70)
    
for _ in range(5):    
    move()
    left()
    move()
    right()



screen = t.Screen()
screen.exitonclick()