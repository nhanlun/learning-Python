import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import numpy as np 

v0 = 10 # initial velocity
mu = 0.01 # resistant constant
m = 1 # weight of the object
g = 9.81 # gravitational acceleration

a = -mu * g
tFinal = - v0 / a

t = np.arange(0, tFinal, 0.1)

sol = np.zeros_like(t)
for i in range(len(t)):
    sol[i] = v0 * t[i] + a * (t[i] ** 2) / 2


fig, ax = plt.subplots()
rectangle = plt.Rectangle((0, 0), 1, 1)
ax.add_patch(rectangle)

def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(-2, 2)
    return rectangle

def run(i):
    ax.set_xlim(sol[i] - 2, sol[i] + 2)
    rectangle.set_xy((sol[i], 0))
    return rectangle

ani = animation.FuncAnimation(fig, run, np.arange(0, len(sol)), init_func=init, interval = 20, repeat = False)

ax.grid()

plt.show()