from turtle import Turtle
FONT = ("Courier", 24, "normal")
DISPLAY_LOCATION = (-280, 265)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.show_current_score()

    def show_current_score(self):
        self.clear()
        self.goto(DISPLAY_LOCATION)
        self.write(arg=f"Level: {self.level}", align="left", font=FONT)

    def update_score(self):
        self.level += 1
        self.show_current_score()

    def game_over(self):
        self.teleport(x=0, y=0)
        self.write(arg="GAME OVER", align="center", font=FONT)
