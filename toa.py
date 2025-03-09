##
## MU TEAM, 2025
## Tower of Angels
## File description:
## Main file for tower of angels
##
from kandinsky import fill_rect
from perf import cap, max_fps

from player import Player

player = Player()

running = True
while running:
    fill_rect(0, 0, 320, 222,"#FFFFFF")

    player.globall()

    cap(30)
