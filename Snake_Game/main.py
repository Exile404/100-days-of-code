from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("ERROR404 Snake Game")
screen.tracer(0)
#CREATE

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

#MOVE

game_on = True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    #Detect Food grab
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increas_score()
    #Detect Collision with wall
    if snake.head.xcor() > 400 or snake.head.xcor() < -401 or snake.head.ycor() > 401 or snake.head.ycor() < -400:
        game_on = False
        scoreboard.game_over()
    for segment in snake.segments[1:]:

        if snake.head.distance(segment) < 5:
            game_on = False
            scoreboard.game_over()




screen.exitonclick()