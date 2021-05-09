def leftRectangle(f, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(n):
        res += f(a + (h * i))
    return res * h


def rightRectangle(f, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(1, n + 1):
        res += f(a + (h * i))
    return res * h


def centralRectangle(f, a, b, n):
    h = (b - a) / n
    res = 0
    for i in range(n):
        res += f(a + (h * (i + 0.5)))
    return res * h


def trapezium(f, a, b, n):
    h = (b - a) / n
    res = (f(a) + f(b)) / 2
    for i in range(1, n):
        res += f(a + (h * i))
    return res * h


def Simpson(f, a, b, n):
    n *= 2
    h = (b - a) / n
    res = f(a) + f(b)

    for i in range(1, n):
        if i % 2 != 0:
            res += 4 * f(a + (h * i))
        else:
            res += 2 * f(a + (h * i))

    return res * h / 3
