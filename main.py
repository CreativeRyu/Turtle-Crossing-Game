import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from gamemap import GameMap

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Objects

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("#9bbc0f")
screen.title("Turtle Crossing Game")
screen.tracer(0)
game_is_on = True
loop_count = 0
cars = []

player = Player()
game_map = GameMap()
car_manager = CarManager()

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Controls

screen.listen()
screen.onkey(player.move, "Up")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.automatic_drive()
    
    if loop_count >= 6: 
        car_manager.create_car()
        loop_count = 0
        
    loop_count += 1


screen.exitonlick()