import matplotlib.pyplot as mp
from math import sin
from numpy import *


def ypp(yp, y, x, k, b, Fo, ω, m):
    ypp = (-k * y - b * yp + Fo * sin(ω * x)) / m
    return ypp


# Numerical Solution # Blue Graph
k = 1
b = 1
Fo = 1
ω = 1
m = 1

y = -1
yp = 1
x = 0
L = 25
n = 1000
del_x = (L - x) / n

xpoints1 = []
ypoints1 = []
xpoints1.append(x)
ypoints1.append(y)

while x <= L:
    y = y + yp * del_x
    yp = yp + ypp(y, yp, x, k, b, Fo, ω, m) * del_x
    x = x + del_x
    xpoints1.append(x)
    ypoints1.append(y)
mp.plot(xpoints1, ypoints1)  # Blue Graph


# Analytical Solution  # Orange Graph
A = 1
ω = 1
x = 0
φ = pi
def f(A, ω, x, φ):
    f = A * cos(ω * x + φ)
    return f


x = linspace(0, L, n)
mp.plot(x, f(A, ω, x, φ))  # Orange Graph
mp.show()
