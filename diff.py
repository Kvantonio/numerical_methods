import numpy as np


def Euler(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, b + h, h)
    Y = np.zeros(len(t))
    Y[0] = y0

    for i in range(0, len(t) - 1):
        Y[i + 1] = Y[i] + h * f(t[i], Y[i])
    return Y.tolist()


def rungeKuttaSecond(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, b + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + (h / 2), y[i] + (k1 / 2))

        y[i + 1] = y[i] + k2

    return y.tolist()


def rungeKuttaThird(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, b + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + (h / 2), y[i] + (k1 / 2))
        k3 = h * f(t[i] + h, y[i] + (k2 * 2) - k1)

        y[i + 1] = y[i] + (k1 + (4 * k2) + k3) / 6

    return y.tolist()


def rungeKuttaFourth(f, a, b, y0, n):
    h = (b - a) / n
    t = np.arange(a, b + h, h)
    y = np.zeros(len(t))
    y[0] = y0
    for i in range(0, len(t) - 1):
        k1 = h * f(t[i], y[i])
        k2 = h * f(t[i] + (h / 2), y[i] + (k1 / 2))
        k3 = h * f(t[i] + (h / 2), y[i] + (k2 / 2))
        k4 = h * f(t[i] + h, y[i] + k3)

        y[i + 1] = y[i] + (k1 + 2 * k2 + 2 * k3 + k4) / 6

    return y.tolist()
