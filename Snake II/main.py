# Import Standard Python Libraries
from turtle import Screen
from time import sleep

# Import Local Python Libraries
from snakeII import SnakeII
from food import Food
from scoreboard import Scoreboard,ArenaBoundary


#Main Function
def arena_setup():
    """ Setup the arena for the game"""
    snake_arena = Screen()
    snake_arena.setup(width=600, height=600)
    snake_arena.bgcolor("#58804D")
    snake_arena.title("Snake")
    snake_arena.tracer(0)
    snake_arena.listen()
    snake_boundary = ArenaBoundary()
    scoreboard = Scoreboard()
    return snake_arena,scoreboard
    
def main():
    """ Main function to run the game"""
    snake_arena,scoreboard = arena_setup()
    snake = SnakeII()
    food = Food()
    game_on = True
    while game_on:
        snake_arena.update()
        snake.move()
        # Detect Wall Collision
        snake.detect_wall_collision()
        # Detect Key Presses
        snake_arena.onkey(snake.up, "Up")
        snake_arena.onkey(snake.down, "Down")
        snake_arena.onkey(snake.left, "Left")
        snake_arena.onkey(snake.right, "Right")
        # Detect Food Consumption
        if snake.snake_head.distance(food) < 15:
            food.move_food()
            snake.create_segment()
            scoreboard.update_score()
            scoreboard.update_high_score()
            if scoreboard.score > 0 and scoreboard.score % 5 == 0:
                snake.increase_speed()
        # Detect Collision with Snake
        if snake.detect_collision():
            scoreboard.game_over()
            game_on = False
        sleep(0.1)
    snake_arena.exitonclick()

# Initialize Screen
if __name__ == "__main__":
    main()
    SystemExit()