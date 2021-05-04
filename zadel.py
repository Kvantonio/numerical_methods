import copy

from dop import isDominant, isPositive

import numpy as np


def zadel(A, B, rd, N=100):
    m = len(A)
    x = [0 for i in range(m)]
    converge = False
    it = 0
    errors = []
    if np.linalg.det(A.copy()) == 0:
        return False, -1

    if not isDominant(A.copy()) and (0 not in np.diag(A)):
        errors.append(-2)

    if not isPositive(A.copy()):
        errors.append(-3)

    if 0 in np.diag(A):
        return False, errors

    while (not converge) and (it <= N):
        x_new = copy.copy(x)
        for i in range(m):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
            x_new[i] = round((B[i] - s1 - s2) / A[i][i], rd)
        pogr = sum(abs(x_new[i] - x[i]) for i in range(m))
        it += 1
        converge = pogr <= pow(1, -(rd+1))

        x = x_new

    err = False
    for i in x:
        if np.isnan(i) or np.isinf(i) or i > 100000 or i < -100000:
            err = True

    if not err:
        return True, [np.round(i, rd) for i in x]
    else:
        return False, errors
