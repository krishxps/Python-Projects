import time
from turtle import Screen
from brain import Food, Scoreboard, Snake

is_on = True

def control():
    scr.listen()
    scr.onkey(snake.up, "w")
    scr.onkey(snake.left, "a")
    scr.onkey(snake.down , "s")
    scr.onkey(snake.right , "d")
    scr.onkey(snake.up, "Up")
    scr.onkey(snake.left, "Left")
    scr.onkey(snake.down , "Down")
    scr.onkey(snake.right , "Right")

scr = Screen()
scr.setup(600,600)
scr.bgcolor("black")
scr.title("My Snake Game")
scr.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
scr.update()
   
control()

while is_on:
    scr.update()
    time.sleep(0.1)
    snake.move()
        
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.score_inc()

    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        is_on = False
        score.game_over()
        
    for segment in snake.segments[1:]:
        
        if snake.head.distance(segment) < 15:
            is_on = False
            score.game_over()
            
scr.exitonclick()
