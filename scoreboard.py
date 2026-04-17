from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Georgia", 18, "bold italic")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.color("#C0C0C0")
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Basilisk Power: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.penup()
        self.write(f"The Chamber Falls Silent", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 1
        self.update_score()

    def reset_score(self):
        self.score = 0
        self.update_score()