from turtle import Screen
from player import Player
from obstacles import Obstacles
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title(titlestring="Turtle Crossing Game")
screen.tracer(0)
screen.colormode(255)

scoreboard = Scoreboard()
player = Player()
obstacles = Obstacles()

screen.listen()
screen.onkey(player.up, "w")
screen.onkey(player.down, "s")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    obstacles.generator()
    obstacles.move()

    for ob in obstacles.all_obstacles:
        if ob.distance(player) < 20:
            scoreboard.game_over()
            game_on = False

    if player.distance(scoreboard) < 15:
        player.refresh()
        scoreboard.refresh()
        obstacles.speed_up()

screen.exitonclick()



