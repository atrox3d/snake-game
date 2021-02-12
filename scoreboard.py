from turtle import Turtle

ALIGN = "center"
FONT =("Arial", 24, "normal")

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def increase(self):
        self.score += 1
        self.update()

