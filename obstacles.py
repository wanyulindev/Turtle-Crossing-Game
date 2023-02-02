from turtle import Turtle
import random

DISTANCE = 5


class Obstacles:

    def __init__(self):
        self.all_obstacles = []
        self.obstacle_speed = DISTANCE

    def generator(self):
        random_chance = random.randint(1, 6)
        if random_chance == 3:
            new = Turtle("square")
            size = random.randint(1, 2)
            new.shapesize(stretch_wid=size, stretch_len=size)
            new.pu()
            rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            new.color(rgb)
            position = (300, random.randint(-200, 200))
            new.goto(position)
            self.all_obstacles.append(new)

    def move(self):
        for ob in self.all_obstacles:
            ob.bk(self.obstacle_speed)

    def speed_up(self):
        self.obstacle_speed += DISTANCE


