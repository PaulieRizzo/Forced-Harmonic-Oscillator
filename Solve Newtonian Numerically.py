"""The three different initial conditions is the c value, changing from -0.5 -> 0.0 -> 0.5 giving us a graph of three
functions.  Being a damped, neutral, and driven harmonic oscillator."""

import numpy as np
from scipy.integrate import odeint
from matplotlib import pyplot as plt

mass = 1.0  # mass constant in kg
k = 3  # some arbitrary constant in N/m
c = -0.5  # some arbitrary constant in N*s/m  c = Fo / (2m*sqrt(k/m))
different_conditions = list()  # a list to keep record of the sets of PositionVelocitys from the three while loops


def harmonic(yvec, time, Ɛ, ω):  # our differential equation
    return yvec[1], -Ɛ * ω * yvec[1] - ω ** 2 * yvec[0]


ω = np.sqrt(k / mass)  # consolidation of terms
time = np.linspace(0, 10, 1000)  # amount of time to record the sets of PositionVelocity
initial_pos_vel = (1, 0)  # the initial position and velocity of the harmonic oscillator

while c <= 0.5:  # our three distinct different initial conditions.
    Ɛ = c / (2 * mass * np.sqrt(k / mass))  # consolidation of terms
    PositionVelocity = odeint(harmonic, initial_pos_vel, time,
                              args=(Ɛ, ω))  # Positions and Velocities over time solved

    different_conditions.append(PositionVelocity)  # keeping record of our Positions and Velocities
    c += 0.5  # starting the next set of our while loop

plt.plot(time, different_conditions[0][:, 0], label='Driven')  # plotting our position from a driving force
plt.plot(time, different_conditions[1][:, 0], label='Neutral')  # plotting our position from a neutral force
plt.plot(time, different_conditions[2][:, 0], label='Damped')  # plotting our position from a damped force
plt.title('Time vs Position')
plt.xlabel('Time')
plt.ylabel('Position')
plt.legend()  # plotting our legend
plt.show()  # plotting our functions

plt.plot(time, different_conditions[0][:, 1], label='Driven')  # plotting our velocity from a driving force
plt.plot(time, different_conditions[1][:, 1], label='Neutral')  # plotting our velocity from a neutral force
plt.plot(time, different_conditions[2][:, 1], label='Damped')  # plotting our velocity from a damped force
plt.title('Time vs Velocity')
plt.xlabel('Time')
plt.ylabel('Velocity')
plt.legend()  # plotting our legend
plt.show()  # plotting our functions

plt.plot(different_conditions[0][:, 0], different_conditions[0][:, 1], label='Driven')  # plotting our velocity from a driving force
plt.plot(different_conditions[1][:, 0], different_conditions[1][:, 1], label='Neutral')  # plotting our velocity from a neutral force
plt.plot(different_conditions[2][:, 0], different_conditions[2][:, 1], label='Damped')  # plotting our velocity from a damped force
plt.title('Position vs Velocity')
plt.xlabel('Position')
plt.ylabel('Velocity')
plt.legend()  # plotting our legend
plt.show()  # plotting our functions


