FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.level_num = 1
        self.goto(-270, 240)
        self.write("Level:", align="left", font=FONT)
        self.goto(-180, 240)
        self.write(self.level_num, align="left", font=FONT)

    def update_level(self):
        self.clear()
        self.goto(-270, 240)
        self.write("Level:", align="left", font=FONT)
        self.goto(-180, 240)
        self.level_num += 1
        self.write(self.level_num, align="left", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME-OVER", align="center", font=FONT)

