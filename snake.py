from turtle import Turtle

STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]

MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake: [Turtle] = []
        self.create_snake()
        self.head: Turtle = self.snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)

    def move(self):
        start = len(self.snake) - 1
        stop = 0
        step = -1
        for segment in range(start, stop, step):
            newx = self.snake[segment - 1].xcor()
            newy = self.snake[segment - 1].ycor()
            self.snake[segment].goto(newx, newy)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


