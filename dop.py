import random

import numpy as np


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
        sum = 0.0
        for j in range(len(A)):
            sum += A[i][j] * X[j]
        res.append(sum)
    return [round(item, len(str(B[i]))) for i, item in enumerate(res)] == B
