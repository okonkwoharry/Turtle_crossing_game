from turtle import Turtle
import random
iCOLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 50



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(iCOLORS))
        self.start_x = 305
        self.start_y = random.randint(-250, 250)
        self.goto(self.start_x, self.start_y)
        self.starting_move_distance = STARTING_MOVE_DISTANCE
        self.move_increment = MOVE_INCREMENT

    def move(self, x):
        self.start_x -= self.starting_move_distance + x
        self.goto(self.start_x, self.start_y)

    def increase_speed(self):
        self.starting_move_distance += self.move_increment




