from dop import isDominant, isPositive, spectralRadius

import numpy as np


def jacobi(A, B, rd, N=1000):
    X = np.zeros(len(A[0]))

    e = float('1e-' + str(rd + 1))

    D = np.diag(A)
    R = A - np.diagflat(D)
    errors = []
    if np.linalg.det(A.copy()) == 0:
        return False, -1

    if not isDominant(A.copy()):
        errors.append(-2)

    if not isPositive(A.copy()):
        errors.append(-3)

    if spectralRadius(A.copy(), 10000000) >= 1:
        errors.append(-4)

    for _ in range(N):
        X2 = (B - np.dot(R, X)) / D

        delta = np.linalg.norm(X - X2)
        if delta < e:
            return True, [np.round(i, rd) for i in X2.tolist()]
        X = X2
    err = False
    for i in X:
        if np.isnan(i) or np.isinf(i) or i > 100000 or i < -100000:
            err = True
    if not err:
        return True, [np.round(i, rd) for i in X2.tolist()]
    else:
        return False, errors
