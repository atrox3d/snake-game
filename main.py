import time
from turtle import Screen
from snake import Snake
#
#   setup screen
#
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()