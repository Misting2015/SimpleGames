from turtle import Turtle
from random import randint, choice
CAR_COLOURS = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "black","brown"]
CAR_LANE = [-250,-220,200,]
CAR_LANE = [-250, -220, -190, -160, -130, -100, -70, -40, -10, 20, 50, 80, 110, 140, 170, 200, 230]


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.cars = []
        self.movement_speed = 10
        self.create_car()
        
    def wave_creator(self):
        car_spawn = self.movement_speed
        if randint(0,car_spawn) >= 9:
            self.create_car()
        
    def create_car(self):
        new_car = Turtle()
        new_car.penup()
        starting_pos_y = choice(CAR_LANE)
        new_car.shape("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(choice(CAR_COLOURS))
        new_car.goto(250,starting_pos_y)
        self.cars.append(new_car)
    
    def move_car(self):
        for i in self.cars:
            i.goto(i.xcor() - self.movement_speed, i.ycor())

        
    def delete_car(self):
        for i in self.cars:
            if i.xcor() < -250:
                i.hideturtle()
                self.cars.remove(i)
    
    def speed_up(self):
        self.movement_speed += 2
        
    def crash(self,player):
        for i in self.cars:
            if player.distance(i) < 20:
                player.goto(0, -280)
                self.movement_speed = 10
                self.cars = []
                return True
        return False
    
        