from turtle import Turtle

STARTING_POSITIONS = [
    (0, 0),
    (-20, 0),
    (-40, 0)
]

MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)

        self.head = self.snake[0]

    def move(self):
        start = len(self.snake) - 1
        stop = 0
        step = -1
        for segment in range(start, stop, step):
            newx = self.snake[segment - 1].xcor()
            newy = self.snake[segment - 1].ycor()
            self.snake[segment].goto(newx, newy)

        self.head.left(90)
        self.head.forward(MOVE_DISTANCE)

