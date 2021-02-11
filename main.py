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
positions = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]

for position in positions:
    segment = Turtle("square")
    segment.color("white")
    segment.goto(position)

screen.exitonclick()