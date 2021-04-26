import numpy as np
import copy


def zadel(A, B, rd):
    m = len(A)
    x = [0 for i in range(m)]
    converge = False

    while not converge:
        x_new = copy.copy(x)
        for i in range(m):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
            x_new[i] = round((B[i] - s1 - s2) / A[i][i], rd)
        pogr = np.sqrt(sum(abs(x_new[i] - x[i]) for i in range(m)))

        converge = pogr < pow(rd, -rd)
        x = x_new
    return x
