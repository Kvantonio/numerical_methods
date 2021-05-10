import base64  # noqa: I201
import random  # noqa: I201
from io import BytesIO  # noqa: I201

import matplotlib.pyplot as plt  # noqa: I201
from matplotlib.patches import Polygon  # noqa: I201
import numpy as np  # noqa: I201


def generate_rand(long, a, b):
    A = [[random.randint(a, b) for _ in range(long)] for _ in range(long)]
    B = [random.randint(a, b) for _ in range(long)]
    return A, B


def parse_file(file):
    with open(file, "r") as f:
        size = int(f.readline())
        lines = f.readlines()
        A = []
        for item in lines:
            parse_line = item.replace("\n", '').split(' ')
            A.append([int(i) for i in parse_line])

        B = [j.pop() for j in A]

    return size, A, B


def isDominant(A):
    res = []
    for j in range(len(A)):
        temp = [abs(i) for i in A[j]]
        res.append(temp)
    a = list(map(sum, res))
    res = [abs(item) >= (a[j] - (abs(item)))
           for j, item in enumerate(np.diag(A))]
    res = True if False not in res else False
    return res


def isPositive(x):
    return np.all(np.linalg.eigvals(x) > 0)


def spectralRadius(mat, k):
    matrix = np.linalg.matrix_power(mat, k)
    f_norm = np.linalg.norm(matrix, 'fro')
    a = f_norm ** (1.0 / k)

    return round(a, 3)


def checkRoots(A, B, X):
    res = []
    for i in range(len(A)):
        s = 0.0
        for j in range(len(A)):
            s += A[i][j] * X[j]
        res.append(s)
    return [round(item) for i, item in enumerate(res)] == B


def graph(x, y):
    fig = plt.figure(figsize=(12, 8))
    plt.plot(x, y, 'ro--')
    plt.grid()
    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    return encoded


def generateIntegration(a, b, f):
    x = np.linspace(a - 0.5, b + 0.5)
    y = f(x)

    fig, ax = plt.subplots()
    ax.plot(x, y, 'r')
    ax.set_ylim(bottom=0)

    # Make the shaded region
    ix = np.linspace(a, b)
    iy = f(ix)
    verts = [(a, 0), *zip(ix, iy), (b, 0)]
    poly = Polygon(verts, facecolor='0.9', edgecolor='0.5')
    ax.add_patch(poly)

    fig.text(0.9, 0.05, '$x$')
    fig.text(0.1, 0.9, '$y$')

    ax.spines.right.set_visible(False)
    ax.spines.top.set_visible(False)
    ax.xaxis.set_ticks_position('bottom')

    ax.set_xticks((a, b))

    ax.set_xticklabels(('$a$', '$b$'))

    tmpfile = BytesIO()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')

    return encoded


def normaliseSets(A, B):
    A = sorted(list(set(filter(lambda x: len(x) > 0, A.split(' ')))))
    B = sorted(list(set(B.split(' '))))
    return A, B
