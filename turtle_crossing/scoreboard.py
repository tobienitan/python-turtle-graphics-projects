from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('black')
        self.penup()

        self.score = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 250)
        self.write(f'level{self.score}', align='center', font=FONT)

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write(f'GAME OVER!', align='center', font=FONT)


