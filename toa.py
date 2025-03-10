##
## MU TEAM, 2025
## Tower of Angels
## File description:
## Main file for tower of angels
##
from kandinsky import fill_rect
from perf import cap, max_fps
from ion import keydown, KEY_OK

from player import Player
from angels import Ruor

player = Player()
test = Ruor(player)
test2 = Ruor(player)

running = True
while running:
    fill_rect(0, 0, 320, 222,"#FFFFFF")

    player.globall()
    test.globall()
    test2.globall()

    if keydown(KEY_OK):
        test.take_damage(player._attack())

    if (player.stats["hp"][0] <= 0):
        print("Game over")
        player.stats["hp"][0] = player.stats["hp"][1]

    print(max_fps())
    cap(20)
