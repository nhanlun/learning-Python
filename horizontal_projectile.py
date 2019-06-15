import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt 

height = 50 # initial height
g = 9.81 # gravitational acceleration
weight = 1 # weigth of the object
vX0 = 10 # initial X velocity
tFinal = np.sqrt(2 * height / g)
t = np.linspace(0, tFinal, int(tFinal) * 50)

fig, ax = plt.subplots()
rec = plt.Rectangle((0, height), 0.5, 0.5)
ax.add_patch(rec)

sol = np.zeros((len(t), 2))

for i in range(len(t)):
    sol[i, 0] = vX0 * t[i]
    sol[i, 1] = height - (1 / 2) * g * t[i] ** 2

print(sol)

def init():
    ax.set_xlim(-2, 2)
    ax.set_ylim(height - 2, height + 2)
    return rec

def run(i):
    ax.set_xlim(sol[i, 0] - 2, sol[i, 0] + 2)
    ax.set_ylim(sol[i, 1] - 2, sol[i, 1] + 2)
    rec.set_xy((sol[i, 0], sol[i, 1]))
    return rec

ani = animation.FuncAnimation(fig, run, np.arange(0, len(t)), init_func=init, interval = 1, repeat = False)

ax.grid()

plt.show()