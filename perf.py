## Perf - Kojiverse Productions
from time import *
from ion import *
from kandinsky import fill_rect

global _FPSs
_FPSs = list(range(30))
global _start_frame
_start_frame = [0]


presses = {key:[None,None] for key in ("KEY_OK","KEY_BACK")}
def presses_update():
  for key in presses.keys():
    presses[key][-2]=presses[key][-1]
    presses[key][-1]=keydown(eval(key))    

click = lambda key:presses[key][-1] and not presses[key][-2]
release = lambda key:presses[key][-2] and not presses[key][-1] 

def get_dir(pos1: list, pos2: list) -> tuple:
    """ Get x and y offset to go from pos1 to pos2 """
    dx: int = pos2[0] - pos1[0]
    dy: int = pos2[1] - pos1[1]
    norm: float = (dy ** 2 + dx ** 2) ** 0.5

    return (dx / norm, dy / norm)

def super_fill_rect(x: int, y: int, width: int, height: int, color: tuple | str) -> None:
   fill_rect(int(x), int(y), int(width), int(height), color)

def max_fps():
  _FPSs.append(monotonic()-_start_frame[0])
  del _FPSs[0]
  _start_frame[0] = monotonic()
  return round(1/(sum(_FPSs)/len(_FPSs)))

def cap(fps):
  while monotonic()-_start_frame[0]<1/fps:
    pass
  _start_frame[0]=monotonic()
  
def collideCircle(circle1, circle2):
    distance_squared = (circle1[0] - circle2[0])**2 + (circle1[1] - circle2[1])**2
    return distance_squared <= (circle1[2] + circle2[2])**2
    
def collideCircleRect(circle, rect):
    distance_squared = (circle[0] - rect[0])**2 + (circle[1] - rect[1])**2

    if distance_squared <= circle[2]**2:
        return True

    x_min, y_min = rect[0], rect[1]
    x_max, y_max = rect[0] + rect[2], rect[1] + rect[3]
    if (x_min - circle[0])**2 + (y_min - circle[1])**2 <= circle[2]**2:
        return True
    if (x_max - circle[0])**2 + (y_min - circle[1])**2 <= circle[2]**2:
        return True
    if (x_min - circle[0])**2 + (y_max - circle[1])**2 <= circle[2]**2:
        return True
    if (x_max - circle[0])**2 + (y_max - circle[1])**2 <= circle[2]**2:
        return True

    return False