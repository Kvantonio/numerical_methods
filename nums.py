import numpy as np
import matplotlib.pyplot as plt
from gauss import gauss
from kramer import kramer
from zadel import zadel
from jordan_gauss import jordan_gauss
from jacobi import jacobi
from dop import generate_rand


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

f1 = lambda x, y: (0.5 * pow(np.exp(x), x)) + x + 1

def Euler(f, a, b, y0, n):
    h = (b - a) / n
    print(np.exp(1.5))
    t = np.arange(0, 1 + h, h)
    Y = np.zeros(len(t))
    Y[0] = y0
    Yt = np.zeros(len(t))
    Yt[0] = y0

    for i in range(0, len(t) - 1):
        Y[i + 1] = Y[i] + h * f(t[i], Y[i])

    plt.figure(figsize=(12, 8))
    plt.plot(t, Y, 'bo--', label='Approximate')
    plt.grid()
    plt.show()
    return Y



print(Euler(lambda x,y: y-x, 0, 1, 1.5, 50))

# print(leftRectangle(2, 5, 5, lambda x: 1 / np.log(x)))
# print(rightRectangle(2, 5, 5, lambda x: 1 / np.log(x)))
# print(centralRectangle(2, 5, 5, lambda x: 1 / np.log(x)))
print(trapezium(2, 5, 10, lambda x: 1 / np.log(x)))
# print(Simpson(2, 5, 10, lambda x: 1 / np.log(x)))
