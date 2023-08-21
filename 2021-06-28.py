import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use("dark_background")

fig = plt.figure()
ax = plt.axes(xlim=(0, 4), ylim=(-3, 3))
plt.axis("off")

(red,) = ax.plot([], [], lw=33, c="#FF0018", zorder=1)
(orange,) = ax.plot([], [], lw=33, c="#FFA52C", zorder=2)
(yellow,) = ax.plot([], [], lw=33, c="#FFFF41", zorder=3)
(green,) = ax.plot([], [], lw=33, c="#008018", zorder=4)
(blue,) = ax.plot([], [], lw=33, c="#0000F9", zorder=5)
(purple,) = ax.plot([], [], lw=23, c="#86007D", zorder=6)
vert = ax.vlines(0.01, -3, 2.1, colors="w", lw=10, zorder=7)


def init():
    red.set_data([], [])
    orange.set_data([], [])
    yellow.set_data([], [])
    green.set_data([], [])
    blue.set_data([], [])
    purple.set_data([], [])
    return (
        red,
        orange,
        yellow,
        green,
        blue,
        purple,
    )


def animate(i):
    x = np.linspace(0, 4, 1000)
    y = -1 + np.sin(0.4 * np.pi * (x - 0.01)) * np.sin(0.05 * i) + 0.075 * np.sin(0.01 * i) + 0.25 * x * np.cos(0.05 * i)
    red.set_data(x, y + 2.5)
    orange.set_data(x, y + 2)
    yellow.set_data(x, y + 1.5)
    green.set_data(x, y + 1)
    blue.set_data(x, y + 0.5)
    purple.set_data(x, y)
    return (
        red,
        orange,
        yellow,
        green,
        blue,
        purple,
    )


anim = FuncAnimation(fig, animate, init_func=init, frames=200, interval=20, blit=True)

anim.save("2021-06-28.gif", writer="imagemagick")
