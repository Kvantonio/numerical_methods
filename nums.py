from gauss import gauss
from kramer import kramer
from zadel import zadel
from jordan_gauss import jordan_gauss
from jacobi import jacobi
import numpy as np
from dop import generate_rand

A = [
    [2, 1, 1],
    [1, -1, 0],
    [3, -1, 2]
    ]

B = [2, -2, 2]


for j in range(1):
    A, B = generate_rand(3, -10, 10)

    for i in A:
        print(i)

    print()
    print(B)
    print()

    print(kramer(A.copy(), B.copy(), 3))
    print(zadel(A.copy(), B.copy(), 3, 1000))
    print(jacobi(A.copy(), B.copy(), 3, 1000))
    print()

