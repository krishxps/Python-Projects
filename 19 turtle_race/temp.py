import turtle as t
import random as r

scr = t.Screen()
scr.setup(width=500 , height=400)

user_bet = scr.textinput(title="Make your choice:",prompt="Which Turtle will win the race? Enter a Color:")
tim1 = t.Turtle(shape='turtle')
tim2 = t.Turtle(shape='turtle')
tim3 = t.Turtle(shape='turtle')
tim4 = t.Turtle(shape='turtle')
tim5 = t.Turtle(shape='turtle')
tim6 = t.Turtle(shape='turtle')
colors = ['blue' , 'red' , 'green' , 'purple' , 'yellow' , 'orange']
turtles = [ tim1 , tim2 , tim3 , tim4 , tim5 , tim6]

tim1.penup()
x = -240
y = -150

for i in range(0,6):
    color = colors[i]
    turtle = turtles[i]
    turtle.speed(2)
    turtle.penup()
    turtle.goto(x,y)
    y += 50
    turtle.color(color)

won = True
while won:
    for i in range(0,6):       
        if turtles[i].xcor() >= 200:
            won = False
            won_color = turtles[i].pencolor()
            if won_color == user_bet:
                print("You Won...!")
            else:
                print(f"You losee {won_color} turtle won..!")
        
        random_walk = r.randint(0,10)
        turtles[i].forward(random_walk)
    
        
