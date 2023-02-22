from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.score_board()

    def score_board(self):
        self.clear()
        self.hideturtle()
        self.penup()
        self.goto(-230, 265)
        self.write(f" Level: {self.level}", align='center', font=FONT)

    def update_score(self):
        self.level +=1
        self.score_board()

    def gameOver(self):
        self.goto(0, 0)

        self.write(arg=f"GAME OVER!", align='center', font=('courier', 20, 'normal'))
