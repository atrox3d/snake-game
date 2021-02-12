import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

#
#   setup screen
#
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase()
        snake.extend()

    if snake.head.xcor() > 280 or \
            snake.head.xcor() < -280 or \
            snake.head.ycor() > 280 or \
            snake.head.ycor() < -280:
        gameon = False
        scoreboard.gameover()

screen.exitonclick()
