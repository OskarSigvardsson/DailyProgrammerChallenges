from __future__ import division, print_function
import sys
import matplotlib.pyplot as plt
import numpy as np

from matplotlib import animation

fig = plt.figure()

ax = plt.axes(xlim=(-5,5), ylim=(-5,5))
ax.grid()

line, = ax.plot([], [])

plt.xticks(np.arange(-5, 5, 1))
plt.yticks(np.arange(-5, 5, 1))

frames = 200
interval = 20
fps = 1000.0/interval 

def init_func():
    line.set_data([], [])

def animate(i):
    y = 5.0*i / frames
    line.set_data([0, 0], [0, y])
    sys.stdout.write(str(i) + "         ")
    sys.stdout.write("\r")

anim = animation.FuncAnimation(fig, animate, frames=frames, interval=1,
    init_func=init_func) 

#anim.save("test.mkv", fps=fps, writer='ffmpeg', codec="ffv1")
plt.show()
