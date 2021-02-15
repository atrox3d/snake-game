from turtle import Turtle

ALIGN = "center"
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.datafile = "data.txt"
        self.highscore = 0
        self.load_highscore()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def load_highscore(self):
        with open("data.txt") as datafile:
            self.highscore = int(datafile.read())

    def save_highscore(self):
        with open("data.txt", mode="w") as datafile:
            datafile.write(f"{self.highscore}")

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.save_highscore()
        self.score = 0
        self.update_score()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)


