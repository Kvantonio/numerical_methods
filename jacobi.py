import numpy as np


def jacobi(A, B, rd, N=1000):
    X = np.zeros(len(A[0]))

    e = float(('1e-') + str(rd + 1))

    D = np.diag(A)
    R = A - np.diagflat(D)

    determ = np.linalg.det(A)

    if determ == 0:
        return -1

    for _ in range(N):
        X2 = (B - np.dot(R, X)) / D
        # if np.isnan(X2[0]):
        #     return -2

        delta = np.linalg.norm(X - X2)
        if delta < e:
            return [np.round(i, rd) for i in X2.tolist()]
        X = X2

    return [np.round(i, rd) for i in X2.tolist()]
