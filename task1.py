import numpy as np
from task1 import sin, cos, pi, sqrt
import matplotlib.pyplot as plt

def graph(alpha0, v0, dt):
    X = []
    Y = []
    t = 0
    v = v0
    vx0 = v0 * cos(alpha0 * pi / 180)
    vy0 = v0 * sin(alpha0 * pi / 180)
    x0 = 0
    y0 = 0
    vx, vy = vx0, vy0
    t = t + dt
    ax = - v * vx
    ay = - 1 - v * vy
    vx = vx0 + ax * dt
    vy = vy0 + ay * dt
    v = sqrt(vx ** 2 + vy **2)
    x = x0 + (vx0 + vx) / 2 + ax * dt * dt / 2
    y = y0 + (vy0 + vy) / 2 + ay * dt * dt / 2
    X.append(x)
    Y.append(y)
    vx0 = vx
    vy0 = vy
    x0 = x
    y0 = y
    text = str(alpha0)
    while y>0:
        t = t + dt
        ax = - v * vx
        ay = - 1 - v * vy
        vx = vx0 + ax * dt
        vy = vy0 + ay * dt
        v = sqrt(vx ** 2 + vy **2)
        x = x0 + (vx0 + vx) / 2 + ax * dt * dt / 2
        y = y0 + (vy0 + vy) / 2 + ay * dt * dt / 2
        X.append(x)
        Y.append(y)
        vx0 = vx
        vy0 = vy
        x0 = x
        y0 = y
    plt.plot(X, Y, label=text+r'$^{\circ}$')

print('Начальная скорость:', end=' ')
v00 = float(input())
print('Шаг изменения времени:', end=' ')
d = float(input())
print('Минимальный угол:', end=' ')
a = int(input())
print('Максимальный угол:', end=' ')
b = int(input())
print('Шаг углов:', end=' ')
s = int(input())

for alpha in range (a, b, s):
    graph(alpha, v00, d)

plt.xlim(0)
plt.ylim(0)
plt.grid(True)
plt.legend()

plt.show()