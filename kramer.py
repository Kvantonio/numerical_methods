import numpy as np
import copy


def kramer(A, B, rd):
    res = []

    if list in (type(A), type(B)):
        B = np.array(B)
        A = np.array(A)

    A = A.swapaxes(0, 1)
    a_s = copy.copy(A)
    determ = np.linalg.det(A)

    if determ == 0:
        return -1

    for j in range(len(A)):
        A = copy.copy(a_s)
        A[j] = B
        te = np.linalg.det(A)
        x = te/determ
        res.append(round(x, rd))

    return res
