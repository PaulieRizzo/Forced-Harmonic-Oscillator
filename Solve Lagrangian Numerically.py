"""

Solving the Lagrangian Numerically, giving us a function for position of time, and we produce
a phase space graph of position vs velocity


Lagrangian Equation:

ℒ = ½mẋ² - ½kx² + xF(t)

where F(t) = Fo * sin(ω * t)

d  (∂ℒ)  _  ∂ℒ  _  0
dt (∂ẋ)     ∂x  ‾¯

The analytic solution to the Lagrangian Equation is seen below.

Differential Equation for a one dimensional simple harmonic oscillator with a force acting upon it:
(Without a damping force b=0)

ẍ + ω²x = F(t) / m

where ω² = k / m

x = position
ẋ = velocity
ẍ = acceleration
t = time
m = mass
k = spring constant
F = force

"""

import numpy as np
from numpy import sin, cos
from scipy.integrate import odeint
from matplotlib import pyplot as plt


# define the equations
def equations(z0, t):
    x, y = z0

    ẏ = [y, F * sin(ω * t) / m - ω ** 2 * x]
    return ẏ


def plot_results(time, PositionVelocity):
    # plt.plot(time, PositionVelocity[:, 0])  # Plotting Time against Position
    # plt.xlabel('time')
    # plt.ylabel('position')
    # plt.grid(True)
    # plt.show()

    plt.plot(PositionVelocity[:, 0], PositionVelocity[:, 1])
    plt.title('Phase Space Diagram')
    plt.xlabel('Position')
    plt.ylabel('Velocity')
    plt.show()


# parameters
F = 5.0
k = 3.0
m = 40.0
ω = np.sqrt(k / m)
x = 0.0

time = np.arange(0, 200.0, 0.025)

# initial conditions
x0 = 0.0  # Initial Height
v0 = 0.0  # Initial Velocity

# find the solution to the differential equation
PositionVelocity = odeint(equations, [x0, v0], time)
velocity = PositionVelocity[:, 1]


# plot the results
plot_results(time, PositionVelocity)
