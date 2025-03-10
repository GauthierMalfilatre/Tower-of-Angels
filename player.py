##
## MU TEAM, 2025
## Tower of Angels
## File description:
## Player class for toa
##
from ion import keydown, KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_OK, KEY_BACK
from kandinsky import fill_rect
from random import randint

"""
stats : 
    atk: int
    tc: float
    dc: float
    pv: list (current, max)
    def: int
    spd: int
"""

class Player:
    def __init__(self, stats: dict = {"atk" : 10, "tc" : 5, "dc" : 30, "pv" : [100, 100], "def" : 10, "spd" : 5}) -> None:
        """ Player variables initialization """
        self.stats = stats
        self.vel = [0, 0]
        self.size = 16
        self.pos = [(320 - self.size) // 2, (222 - self.size) // 2]

    def __move(self) -> None:
        """ Player movement """
        self.vel = [0, 0]

        if keydown(KEY_UP):
            self.vel[1] = -1
        elif keydown(KEY_DOWN):
            self.vel[1] = 1

        if keydown(KEY_RIGHT):
            self.vel[0] = 1
        elif keydown(KEY_LEFT):
            self.vel[0] = -1

        self.pos[0] += self.vel[0] * self.stats["spd"]
        self.pos[1] += self.vel[1] * self.stats["spd"]

        return
    
    def __attack(self) -> int:
        if not keydown(KEY_OK):
            return 0
        a = randint(0, 100)
        is_critical = a <= self.stats["tc"]
        damages = self.stats["atk"] * (1 + ((self.stats["dc"] / 100) if is_critical else 0))

        print("Attack : damage deal = %d, is_critical = %d, a = %d"%(damages, is_critical, a))

        return 1

    def _render(self) -> None:
        """ Player render """
        fill_rect(self.pos[0], self.pos[1], self.size, self.size, "#FF0000")

    def globall(self):
        """ Global player call """
        self.__move()
        self.__attack()
        self._render()
