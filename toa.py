##
## MU TEAM, 2025
## Tower of Angels
## File description:
## Main file for tower of angels
##
from kandinsky import fill_rect
from perf import cap, max_fps

from player import Player
from angels import Ruor

player = Player()
test = Ruor(player)

running = True
while running:
    fill_rect(0, 0, 320, 222,"#FFFFFF")

    player.globall()
    test.globall()

    cap(20)
