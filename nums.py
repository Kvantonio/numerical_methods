from gauss import gauss
from kramer import kramer
from zadel import zadel
from jordan_gauss import jordan_gauss
from jacobi import jacobi
from dop import generate_rand


A = [
    [2, 1, 1],
    [1, -1, 0],
    [3, -1, 2]
    ]

B = [2, -2, 2]


for j in range(10):
    A, B = generate_rand(3, -10, 10)

    for i in A:
        print(i)

    print()
    print(B)
    print()

    print(kramer(A.copy(), B.copy(), 5))
    print(gauss(A.copy(), B.copy(), 5))
    print(jordan_gauss(A.copy(), B.copy(), 5))
    print(zadel(A.copy(), B.copy(), 4, 1000))
    print(jacobi(A.copy(), B.copy(), 4, 1000))
    print()
