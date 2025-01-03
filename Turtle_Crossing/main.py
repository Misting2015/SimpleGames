from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager
from time import sleep

def main_loop():
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    game_on = True
    player = Player()
    scoreboard = Scoreboard()
    car_manager = CarManager()
    while game_on == True:
        screen.onkeypress(key="Up",fun=player.move_up)
        screen.onkeypress(key="Down",fun=player.move_down)
        car_manager.move_car()

        car_manager.wave_creator()
        if player.ycor() > 250:
            player.next_level()
            scoreboard.level += 1
            scoreboard.update_scoreboard()
            car_manager.speed_up()
        if car_manager.crash(player):
            print("Game Over")
            game_on = False
            scoreboard.level = 1
            scoreboard.update_scoreboard()
        screen.update()
        sleep(0.1)
        
    screen.exitonclick()


if __name__ == "__main__":
    main_loop()
    SystemExit(0)
    