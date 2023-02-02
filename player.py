from turtle import Turtle

MOVE_DISTANCE = 10
UP = 90
POSITION = (0, -250)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.pu()
        self.color("olive")
        self.seth(UP)
        self.goto(POSITION)

    def up(self):
        self.fd(MOVE_DISTANCE)

    def down(self):
        self.bk(MOVE_DISTANCE)

    def refresh(self):
        self.goto(POSITION)



