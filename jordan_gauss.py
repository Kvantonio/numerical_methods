import numpy as np


def pick_nonzero_row(m, k):
    while k < m.shape[0] and not m[k, k]:
        k += 1
    return k


def jordan_gauss(A, B, rd):
    n = len(A)

    if list in (type(A), type(B)):
        B = np.array(B)
        A = np.array(A)

    determ = np.linalg.det(A)
    if determ == 0:
        return -1

    m = np.hstack((A, np.array(np.diag([1.0 for i in range(A.shape[0])]))))

    for k in range(n):
        # 1) Swap k-row with one of the underlying if m[k, k] = 0
        swap_row = pick_nonzero_row(m, k)
        if swap_row != k:
            m[k, :], m[swap_row, :] = m[swap_row, :], np.copy(m[k, :])
        # 2) Make diagonal element equals to 1
        if m[k, k] != 1:
            m[k, :] *= 1 / m[k, k]
        # 3) Make all underlying elements in column equal to zero
        for row in range(k + 1, n):
            m[row, :] -= m[k, :] * m[row, k]

    for k in range(n - 1, 0, -1):
        for row in range(k - 1, -1, -1):
            if m[row, k]:
                # 1) Make all overlying elements equal to zero
                # in the former identity matrix
                m[row, :] -= m[k, :] * m[row, k]

    A_inv = np.hsplit(m, 2)[1]

    res = [round(i, rd) for i in (A_inv @ B).tolist()]
    return res
