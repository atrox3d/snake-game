import time
from turtle import Turtle, Screen
#
#   setup screen
#
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
#
#   create snake body
#
positions = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]

snake = []

for position in positions:
    segment = Turtle("square")
    segment.color("white")
    segment.penup()
    segment.goto(position)
    snake.append(segment)


gameon = True
head = snake[0]
while gameon:
    screen.update()
    time.sleep(0.1)

    for segment in range(len(snake)-1, 0, -1):
        newx = snake[segment - 1].xcor()
        newy = snake[segment - 1].ycor()
        snake[segment].goto(newx, newy)

    head.left(90)
    head.forward(20)



screen.exitonclick()