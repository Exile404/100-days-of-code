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
        scoreboard.increas_score()




screen.exitonclick()