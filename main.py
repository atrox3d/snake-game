from turtle import Turtle, Screen
#
#   setup screen
#
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
#
#   create snake body
#
snake = []
offset = 0
for _ in range(3):
    s = Turtle("square")
    s.color("white")
    s.penup()
    s.setx(offset)
    snake.append(s)
    offset -= 20


screen.exitonclick()