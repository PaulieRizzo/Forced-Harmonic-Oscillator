import matplotlib.pyplot as mp
from math import sqrt, exp, log, sin, cos
from numpy import *


def ypp(yp, y, x):
    ypp = 2 * x - y - yp
    return ypp


# Numerical Solution # Blue Graph
y = 0
yp = 2
x = 0
L = 10
n = int(input("How many sub-intervals? (Higher number, greater accuracy) "))
del_x = (L - x) / n

xpoints1 = []
ypoints1 = []
xpoints1.append(x)
ypoints1.append(y)

while x <= L:
    y = y + yp * del_x
    yp = yp + ypp(y, yp, x) * del_x
    x = x + del_x
    xpoints1.append(x)
    ypoints1.append(y)
mp.plot(xpoints1, ypoints1)  # Blue Graph


# Analytical Solution  # Orange Graph
def f(x):
    f = (2 * x) + (4 * exp(-x / 2) * cos((sqrt(3) * x) / 2) + (4 / sqrt(3))) * exp(-x / 2) * sin((sqrt(3) * x) / 2) - 2
    return f


x = linspace(0, L, n)
mp.plot(x, f(x))  # Orange Graph
mp.show()
