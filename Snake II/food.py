from turtle import Turtle
from random import randint

class Food(Turtle):
    
    def __init__(self):
        """ Initialize the Food class"""
        super().__init__()
        self.shape("circle")
        self.color("black")
        self.shapesize(0.5,0.5)
        self.penup()
        self.move_food()
        
    def move_food(self):
        """ Move the food to a new location"""
        x_cor = randint(-280, 280)
        y_cor = randint(-280, 280)
        self.goto(x_cor, y_cor)