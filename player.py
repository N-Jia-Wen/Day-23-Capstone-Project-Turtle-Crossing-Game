from turtle import Turtle
STARTING_POS = (0, -280)
MOVE_DIST = 10
UP = 90


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.return_start()

    def return_start(self):
        self.goto(STARTING_POS)
        self.setheading(UP)

    def player_move(self):
        self.forward(MOVE_DIST)
