import re
import sys
from dataclasses import dataclass

import matplotlib.pyplot as plt
import numpy as np

data = open("data/p14.txt").read().strip().splitlines()
shape = np.array([101, 103])


@dataclass
class Bot:
    p: np.ndarray
    v: np.ndarray


bots = [
    Bot(p=np.array(xs[:2]), v=np.array(xs[2:]))
    for xs in [[int(x) for x in re.findall(r"-?\d+", line)] for line in data]
]

frame = 0


def grid():
    g = np.zeros(shape, dtype=int)
    for bot in bots:
        g[tuple(bot.p)] += 1
    return g


def forward_frame():
    for bot in bots:
        bot.p += bot.v
        bot.p %= shape


def backward_frame():
    for bot in bots:
        bot.p -= bot.v
        bot.p %= shape


frame = 0
interesting_frames = [63, 82]
periods = [103, 101]


def next_interesting():
    global frame
    while frame < min(interesting_frames):
        forward_frame()
        frame += 1
    if interesting_frames[0] < interesting_frames[1]:
        interesting_frames[0] += periods[0]
    else:
        interesting_frames[1] += periods[1]


def prev_intresting():
    global frame
    if interesting_frames[0] < interesting_frames[1]:
        interesting_frames[1] -= periods[1]
    else:
        interesting_frames[0] -= periods[0]

    while frame > min(interesting_frames):
        backward_frame()
        frame -= 1


def on_press(event):
    print("press", event.key)
    if event.key == "right":
        next_interesting()
    elif event.key == "left":
        prev_intresting()
    ax.set_title(f"frame {frame}")
    img.set_data(grid())
    ax.figure.canvas.draw_idle()
    sys.stdout.flush()


fig, ax = plt.subplots()
fig.canvas.mpl_connect("key_press_event", on_press)
img = ax.imshow(grid(), cmap="viridis")
plt.show()
