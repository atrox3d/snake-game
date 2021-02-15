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
    #
    #   detect food collision
    #
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend()
    #
    #   detect wall collision
    #
    if snake.head.xcor() > 280 or \
            snake.head.xcor() < -280 or \
            snake.head.ycor() > 280 or \
            snake.head.ycor() < -280:
        scoreboard.reset_score()
        snake.reset_snake()
    #
    #   detect tail collision
    #
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset_snake()

screen.exitonclick()
