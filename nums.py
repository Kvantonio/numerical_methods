import numpy as np
import matplotlib.pyplot as plt
from gauss import gauss
from kramer import kramer
from zadel import zadel
from jordan_gauss import jordan_gauss
from jacobi import jacobi
from dop import generate_rand


def graph(x, y):
    plt.figure(figsize=(12, 8))
    plt.plot(x, y, 'ro--')
    plt.grid()
    plt.savefig('static/graph.png')


def fr(x, y):
    return x + y


def leftRectangle(a, b, n, f):
    h = (b - a) / n
    res = 0
    for i in range(n):
        res += f(a + (h * i))
    return res * h


def rightRectangle(a, b, n, f):
    h = (b - a) / n
    res = 0
    for i in range(1, n + 1):
        res += f(a + (h * i))
    return res * h


def centralRectangle(a, b, n, f):
    h = (b - a) / n
    res = 0
    for i in range(n):
        res += f(a + (h * (i + 0.5)))
    return res * h


def trapezium(a, b, n, f):
    h = (b - a) / n
    res = (f(a) + f(b)) / 2
    for i in range(1, n):
        res += f(a + (h * i))
    return res * h


def Simpson(a, b, n, f):
    n *= 2
    h = (b - a) / n
    res = f(a) + f(b)

    for i in range(1, n):
        if i % 2 != 0:
            res += 4 * f(a + (h * i))
        else:
            res += 2 * f(a + (h * i))

    return res * h / 3


def Euler(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, 1 + h, h)
    Y = np.zeros(len(t))
    Y[0] = y0

    for i in range(0, len(t) - 1):
        Y[i + 1] = Y[i] + h * f(t[i], Y[i])

    plt.figure(figsize=(12, 8))
    plt.plot(t, Y, 'bo--')
    plt.grid()
    plt.savefig('static/graf.png')

    return Y.tolist()


def rungeKuttaSecond(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, 1 + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + (h / 2), y[i] + (k1 / 2))

        y[i + 1] = y[i] + k2

    graph(t, y)
    return y.tolist()


def rungeKuttaThird(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, 1 + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + (h / 2), y[i] + (k1 / 2))
        k3 = h * f(t[i] + h, y[i] + (k2 * 2) - k1)

        y[i + 1] = y[i] + (k1 + (4 * k2) + k3) / 6

    graph(t, y)
    return y.tolist()


def rungeKuttaFourth(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, 1 + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + (h / 2), y[i] + (k1 / 2))
        k3 = h * f(t[i] + (h / 2), y[i] + (k2 / 2))
        k4 = h * f(t[i] + h, y[i] + k3)

        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    graph(t, y)
    return y.tolist()


# f2 = lambda x, y: x + y
# f1 = lambda x, y: -1 * (x * y)
# f3 = lambda x, y: (3*x - 12*x*x) * y
#
# print(Euler(lambda x, y: 2 * x * y, 0, 1, 1, 10))
print(rungeKuttaSecond(lambda x, y: 2 * x * y, 0, 1, 1, 10))
print(rungeKuttaThird(lambda x, y: 2 * x * y, 0, 1, 1, 10))
print(rungeKuttaFourth(lambda x, y: 2 * x * y, 0, 1, 1, 10))
# print(leftRectangle(2, 5, 5, lambda x: 1 / np.log(x)))
# print(rightRectangle(2, 5, 5, lambda x: 1 / np.log(x)))
# print(centralRectangle(2, 5, 5, lambda x: 1 / np.log(x)))
# print(trapezium(2, 5, 10, lambda x: 1 / np.log(x)))
# print(Simpson(2, 5, 10, lambda x: 1 / np.log(x)))
