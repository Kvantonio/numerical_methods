import copy

import numpy as np


def kramer(A, B, rd):
    res = []

    if list in (type(A), type(B)):
        B = np.array(B)
        A = np.array(A)

    A = A.swapaxes(0, 1)
    a_s = copy.copy(A)
    det = np.linalg.det(A)
    if det == 0:
        return -1

    for j in range(len(A)):
        A = copy.copy(a_s)
        A[j] = B
        te = np.linalg.det(A)
        x = te/det
        res.append(round(x, rd))

    return res
