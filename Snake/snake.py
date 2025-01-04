from turtle import Turtle

class Snake(Turtle):
    
    def __init__(self):
        """ Initialize the Snake class """
        self.snake = []
        self.create_snake()
        self.snake[0].color("green")
        self.movement_increment = 10
        
    def create_snake(self):
        """ Create the snake at the commencments of the game"""
        self.snake_head = Turtle()
        self.snake_head.shape("square")
        self.snake_head.color("black")
        self.snake_head.penup()
        self.snake.append(self.snake_head)
        for i in range(2):
            self.create_segment()
            
    def create_segment(self):
        """ Create a new segment for the snake"""
        snake_segment = Turtle()
        snake_segment.shape("square")
        snake_segment.color("black")
        snake_segment.penup()
        snake_segment.goto(self.snake[-1].xcor(), self.snake[-1].ycor())
        self.snake.append(snake_segment)
            
    def move(self):
        """ Move the snake forward automatically"""
        for i in range(len(self.snake)-1, 0, -1):
            new_x = self.snake[i-1].xcor()
            new_y = self.snake[i-1].ycor()
            self.snake[i].goto(new_x, new_y)
        self.snake_head.forward(self.movement_increment)
        
    def up(self):
        """ Move the snake up"""
        if self.snake_head.heading() == 270:
            return
        self.snake_head.setheading(90)
        
    def down(self):
        """ Move the snake down"""
        if self.snake_head.heading() == 90:
            return
        self.snake_head.setheading(270)
        
    def left(self):
        """ Move the snake left"""
        if self.snake_head.heading() == 0:
            return
        self.snake_head.setheading(180)
    
    def right(self):
        """ Move the snake right"""
        if self.snake_head.heading() == 180:
            return
        self.snake_head.setheading(0)
        
    def increase_speed(self):
        """ Increase the speed of the snake"""
        self.movement_increment += 0.1
        
    def detect_collision(self):
        """ Detect if the snake collides with itself"""
        for segment in self.snake[1:]:
            if self.snake_head.xcor() == segment.xcor() and self.snake_head.ycor() == segment.ycor():
                return True
        return False