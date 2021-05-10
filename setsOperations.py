def entrance(A, B):
    while A and B:
        if A[0] < B[0]:
            return False
        elif A[0] > B[0]:
            B.remove(B[0])
        else:
            A.remove(A[0])
            B.remove(B[0])

    return A == []


def merge(A, B):
    i = 0
    res = []
    while i <= len(A) - 1 and i <= len(B) - 1:
        if A[0] < B[i]:
            res.append(A[i])
            A.remove(A[i])
        elif A[i] > B[i]:
            res.append(B[i])
            B.remove(B[i])
        else:
            res.append(A[i])
            A.remove(A[i])
            B.remove(B[i])

    if A:
        res += A
    if B:
        res += B
    return res


def traversal(A, B):
    i = 0
    j = 0
    res = []
    while i <= len(A) - 1 and j <= len(B) - 1:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            res.append(A[i])
            i += 1
            j += 1
    return res


def difference(A, B):
    i = 0
    j = 0
    res = []
    while i <= len(A) - 1 and j <= len(B) - 1:
        if A[i] < B[j]:
            res.append(A[i])
            A.remove(A[i])
        elif A[i] > B[j]:
            j += 1
        else:
            A.remove(A[i])
            B.remove(B[j])

    if A:
        res += A

    return res


def symmetricalDifference(A, B):
    i = 0
    res = []
    while i <= len(A) - 1 and i <= len(B) - 1:
        if A[i] < B[i]:
            res.append(A[i])
            A.remove(A[i])
        elif A[i] > B[i]:
            res.append(B[i])
            B.remove(B[i])
        else:
            A.remove(A[i])
            B.remove(B[i])

    if A:
        res += A
    if B:
        res += B

    return res
