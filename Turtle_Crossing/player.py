# Import Python Standard Libraries
from turtle import Turtle
import random


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.initialize_player()
        
    def initialize_player(self):
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(0, -280)
        
    def move_up(self):
        new_y = self.ycor() + 20
        self.sety(new_y)
        
    def move_down(self):
        new_y = self.ycor() - 20
        self.sety(new_y)
        
    def next_level(self):
        self.goto(0, -280)
        self.initialize_player()
