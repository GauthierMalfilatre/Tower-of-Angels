##
## MU TEAM, 2025
## Tower of Angels
## File description:
## Player class for toa
##
from ion import keydown, KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN, KEY_OK, KEY_BACK
from kandinsky import fill_rect
from random import randint
from time import monotonic
from sprites import archangel, draw_sprite, colors
from perf import collideRect

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
    def __init__(self, level: int = 0, stats: dict = {"atk" : 10, "tc" : 5, "dc" : 30, "hp" : [100, 100], "def" : 10, "spd" : 5}, targets: list = []) -> None:
        """ Player variables initialization """
        self.stats = stats
        self.vel = [0, 0]
        self.size = 16
        self.level = level
        self.pos = [(320 - self.size) // 2, (222 - self.size) // 2]
        self.delay = [0, 0.5]
        self.sword = [0, 0]
        self.cooldown = [0, 0.5]
        self.targets = targets

    def _rect(self) -> tuple:
        return (self.pos[0], self.pos[1], self.size, self.size)

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

        if keydown(KEY_OK):
            self._attack()

        self.pos[0] += self.vel[0] * self.stats["spd"]
        self.pos[1] += self.vel[1] * self.stats["spd"]

        return

    def _attack(self) -> int:
        """ Take damage and deal with def """
        if self.cooldown[0]:
            return 1

        for target in self.targets:
            if collideRect(self._rect(), target._rect()):
                a = randint(0, 100)
                is_critical = a <= self.stats["tc"]
                damages = self.stats["atk"] * (1 + ((self.stats["dc"] / 100) if is_critical else 0))
                target.take_damage(damages)
                print("deal %d damages to %s"%(damages, target))
                self.cooldown[0] = monotonic()
        return 0

    def _render(self) -> None:
        """ Player render """
        fill_rect(self.pos[0], self.pos[1], self.size, self.size, "#FF0000")
        # draw_sprite(archangel, colors["samael"], int(self.pos[0]), int(self.pos[1]), 1)

    def take_damage(self, damages: int) -> int:
        if self.delay[0]:
            return 1

        self.stats["hp"][0] -= (damages * 1 - self.stats["def"] / 1000)
        print("Taken %d damages!"%(damages * 1 - self.stats["def"] / 1000))
        self.delay[0] = monotonic()
        return 0

    def globall(self):
        """ Global player call """
        if monotonic() - self.delay[0] > self.delay[1]:
            self.delay[0] = 0
        if monotonic() - self.cooldown[0] > self.cooldown[1]:
            self.cooldown[0] = 0

        self.__move()
        self._render()
