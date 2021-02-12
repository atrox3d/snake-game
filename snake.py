from turtle import Turtle


class Snake:

    def __init__(self):
        #   create snake body
        #
        self.positions = [
            (0, 0),
            (-20, 0),
            (-40, 0)
        ]

        self.snake = []
        for position in self.positions:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.snake.append(segment)

        self.head = self.snake[0]

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            newx = self.snake[segment - 1].xcor()
            newy = self.snake[segment - 1].ycor()
            self.snake[segment].goto(newx, newy)

        self.head.left(90)
        self.head.forward(20)

