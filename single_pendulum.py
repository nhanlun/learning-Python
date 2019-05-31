import matplotlib.animation as animation
import matplotlib.pyplot as plt 
import numpy as np 
from scipy.integrate import odeint 

theta = 180 # initial angle
omega = 0 # initial angle velocity
b = 0.5 # air resitance
g = 9.81 # gravitational acceleration
l = 2 # length of the rope


period = 2 * np.pi * np.sqrt(l / g)
t = np.arange(0, period * 50, 0.1)

# differential equation
def pend(state, t, b, g, l): 
    theta, omega = state
    dydx = [omega, -b * omega - g / l * np.sin(theta)]
    return dydx


y0 = [np.radians(theta), omega] # initial condition

sol = odeint(pend, y0, t, args=(b, g, l))

x = l * np.sin(sol[:, 0])
y = -l * np.cos(sol[:, 0])

fig, ax = plt.subplots()
ax.grid()
line, = plt.plot([], [], 'o-', lw = 2)


def init():
    ax.set_xlim(- l - 0.5, l + 0.5)
    ax.set_ylim(-l - 0.5, l + 0.5)
    line.set_data([], [])
    return line


def calc(i):
    thisX = [0, x[i]]
    thisY = [0, y[i]]
    line.set_data(thisX, thisY)
    return line

ani = animation.FuncAnimation(fig, calc, np.arange(0, len(x)), init_func=init, interval = 5)

plt.show()