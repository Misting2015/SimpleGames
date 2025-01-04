from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.get_high_score()
        self.create_scoreboard()
        
    def get_high_score(self):
        """ Get the high score from the data.txt file"""
        with open("Snake\data.txt", "r") as file:
            self.high_score = int(file.read())
    
    
    def create_scoreboard(self):
        """ Create the scoreboard at the top of the screen"""
        self.penup()
        self.goto(0,260)
        self.write(f"Score: {self.score} \t High Score: {self.high_score}", align="center", font=("Arial", 14, "normal"))
        self.penup()

    def update_score(self):
        """ Update the score on the screen"""
        self.score += 1
        self.update_high_score()
        self.clear()
        self.write(f"Score: {self.score} \t High Score: {self.high_score}", align="center", font=("Arial", 14, "normal"))
    
    def game_over(self):
        """ Display Game Over on the screen"""
        self.goto(0,0)
        self.write("Game Over", align="center", font=("Arial", 24, "normal"))
    
    def update_high_score(self):
        """ Update the high score in the data.txt file"""
        if self.score > self.high_score:
            with open("Snake\data.txt", "w") as file:
                file.write(str(self.score))
            self.high_score = self.score

class ArenaBoundary(Turtle):
    
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.speed(0)
        self.pensize(5)
        self.draw_boundary()

    def draw_boundary(self):
        """ Draw the boundary of the arena"""
        self.goto(-295, 295)
        self.pendown()
        self.goto(295, 295)
        self.goto(295, -295)
        self.goto(-295, -295)
        self.goto(-295, 295)
        self.penup()
        
