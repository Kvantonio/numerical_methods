def normaliseSets(A, B):
    A = sorted(list(set(A)))
    B = sorted(list(set(B)))

    return A, B


def entrance(A, B):
    i = 0
    j = 0
    while i <= len(A)-1 and j <= len(B)-1:
        if A[i] < B[j]:
            return False
        elif A[i] > B[j]:
            j += 1
        else:
            i += 1
            j += 1

    return True


def merge(A, B):
    i = 0
    res = []
    while i <= len(A)-1 and i <= len(B)-1:
        if A[i] < B[i]:
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
    while i <= len(A)-1 and j <= len(B)-1:
        if A[i] < B[j]:
            i += 1
        elif A[i] > B[j]:
            j += 1
        else:
            res.append(A[i])
            i += 1
            j += 1
    return res

A = ['a', 'c', 'b', 'd']
B = ['d', 'c', 'e', 'f', 'g']


print(A)
print(B)
A, B = normaliseSets(A, B)
print(entrance(A, B))
print(merge(A.copy(), B.copy()))
print(traversal(A.copy(), B.copy()))


