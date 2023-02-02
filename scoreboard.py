from turtle import Turtle

# ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')
# DEFAULT = (0, 260)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("light salmon")
        self.ht()
        self.pu()
        self.goto(0, 260)
        self.show()

    def show(self):
        self.clear()
        self.write(f"Level: {self.level}", font=FONT, align="center")

    def refresh(self):
        self.level += 1
        self.show()

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"Game Over..", font=FONT, align="center")








