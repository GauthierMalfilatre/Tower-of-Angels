##
## MU TEAM, 2025
## Tower of Angels
## File description:
## Monster class for toa
##
from kandinsky import fill_rect, draw_string
from random import randint, random, uniform
from perf import get_dir, super_fill_rect
from time import monotonic

from player import Player

"""
stats:
    hp: list [current, max]
    atk: int
    spd: int
    def: int
"""

class Angels:
    def __init__(self, target: Player, stats: dict = {"hp" : [20, 20], "atk" : 10, "spd" : 2, "def" : 0}, size: int = 16) -> None:
        """ Initialization of variables for monsters """
        self.stats = stats
        self.size = size
        self.pos = [randint(1, 310), randint(1, 210)]
        self.vel = [0, 0]
        self.target = target

    def render(self):
        """ Angels global render """
        super_fill_rect(self.pos[0], self.pos[1], self.size, self.size, "#00FF00")

class Ruor(Angels):
    def __init__(self, target: Player | Angels, stats = { "hp": [20, 20],"atk": 10,"spd": 2,"def": 0 }, size = 16):
        """ Ruor variable initialization """
        super().__init__(target, stats, size)
        self.charge = False
        self.charge_target = [0, 0]
        self.start_of_charge = 0

    def move(self) -> None:
        """ Ruor movements """

        if not self.charge and random() < 0.1:
            self.charge = True
            self.start_of_charge = monotonic()
            self.charge_target = get_dir(self.pos, self.target.pos)

        if (self.charge and monotonic() - self.start_of_charge > 2):
            self.charge = False

        self.vel = get_dir(self.pos, self.target.pos) if not self.charge else self.charge_target

        self.pos[0] += self.vel[0] * self.stats["spd"] * (1 + self.charge) + (uniform(-1, 1) if not self.charge else 0)
        self.pos[1] += self.vel[1] * self.stats["spd"] * (1 + self.charge) + (uniform(-1, 1) if not self.charge else 0) 

        return

    def globall(self) -> None:
        self.move()
        self.render()
