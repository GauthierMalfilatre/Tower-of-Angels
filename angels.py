##
## MU TEAM, 2025
## Tower of Angels
## File description:
## Monster class for toa
##
from kandinsky import fill_rect, draw_string
from random import randint, random, uniform
from perf import get_dir, super_fill_rect, collideRect
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
    def __init__(self, target: Player, level: int = 1, stats: dict = {"hp" : [20, 20], "atk" : 1, "spd" : 2, "def" : 0}, size: int = 16) -> None:
        """ Initialization of variables for monsters """
        self.stats = stats
        self.size = size
        self.pos = [randint(10, 300), randint(10, 200)]
        self.vel = [0, 0]
        self.last_damages = 0
        self.target = target
        self.level = level
        self.delay = [0, 0.5]

    def on_damage(self) -> None:
        """ Draw a string with damages takens """
        if self.delay[0]:
            x = self.pos[0] + self.size / 2 - len(str(self.last_damages) * 7) / 2
            y = self.pos[1] - 20
            draw_string(str(int(self.last_damages)), int(x), int(y), "#FF0000")
        if monotonic() - self.delay[0] > self.delay[1]:
            self.delay[0] = 0

    def damage_on_target(self, factor: float = 1) -> int:
        """ Deal damages when on target """
        if collideRect((self.pos[0], self.pos[1], self.size, self.size), (self.target.pos[0], self.target.pos[1], self.target.size, self.target.size)):
            self.target.take_damage(self.stats["atk"] * factor)
            return 1
        return 0

    def take_damage(self, damages: int) -> int:
        """ Take damage and feal with def """
        if self.delay[0]:
            return 1

        self.last_damages = (damages * 1 - self.stats["def"] / 1000)
        self.stats["hp"][0] -= self.last_damages
        print("Angel takes %d damages!"%(damages * 1 - self.stats["def"] / 1000))
        self.delay[0] = monotonic()
        return 0

    def render(self):
        """ Angels global render """
        super_fill_rect(self.pos[0], self.pos[1], self.size, self.size, "#00FF00")

class Ruor(Angels):
    def __init__(self, target: Player | Angels, level: int = 0, stats = { "hp": [20, 20], "atk": 5,"spd": 2,"def": 0 }, size = 16):
        """ Ruor variable initialization """
        super().__init__(target, level, stats, size)
        self.charge = False
        self.charge_target = [0, 0]
        self.start_of_charge = 0
        self.delay = [0, 0]

    def move(self) -> None:
        """ Ruor movements """
        if not self.charge and random() < 0.02:
            self.charge = True
            self.start_of_charge = monotonic()
            self.charge_target = get_dir(self.pos, self.target.pos)

        if (self.charge and monotonic() - self.start_of_charge > 2):
            self.charge = False

        self.vel = get_dir(self.pos, self.target.pos) if not self.charge else self.charge_target
        x = self.vel[0] * self.stats["spd"] * (1 + self.charge * 2) + (uniform(-1, 1) if not self.charge else 0)
        y = self.vel[1] * self.stats["spd"] * (1 + self.charge * 2) + (uniform(-1, 1) if not self.charge else 0)

        if (10 < self.pos[0] + x < 300):
            self.pos[0] += x
        if (10 < self.pos[1] + y < 200):
            self.pos[1] += y

        return

    def globall(self) -> None:
        self.move()
        self.render()
        self.damage_on_target(1 + self.charge)
        self.on_damage()
