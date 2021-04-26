import random

from gauss import gauss
from kramer import kramer
from zadel import zadel
from jordan_gauss import jordan_gauss


def generate_rand(l, a, b):
    A = [[random.randint(a, b) for _ in range(l)] for _ in range(l)]
    B = [random.randint(a, b) for _ in range(l)]
    return(A, B)


A = [
    [2, 1, 1],
    [1, -1, 0],
    [3, -1, 2]
    ]

B = [2, -2, 2]

A, B = generate_rand(8, 1, 20)

for i in A:
    print(i)

print()
print(B)
print()

print(kramer(A.copy(), B.copy(), 5))
print(gauss(A.copy(), B.copy(), 5))
print(zadel(A, B, 5))
print(jordan_gauss(A.copy(), B.copy(), 5))
