import random
from gauss import gauss
from kramer import kramer
from zadel import zadel
from jordan_gauss import jordan_gauss
from jacobi import jacobi


def generate_rand(l, a, b):
    A = [[random.randint(a, b) for _ in range(l)] for _ in range(l)]
    B = [random.randint(a, b) for _ in range(l)]
    return(A, B)


def parse_file(file):
    with open(file, "r") as f:
        lines = f.readlines()[1:]
        A = []
        for item in lines:
            parse_line = item.replace("\n", '').split(' ')
            A.append([float(i) for i in parse_line])

        B = [j.pop() for j in A]

    return (A, B)


A = [
    [2, 1, 1],
    [1, -1, 0],
    [3, -1, 2]
    ]

B = [2, -2, 2]

A, B = parse_file("te.txt")
A, B = generate_rand(3, 1, 10)

for i in A:
    print(i)

print()
print(B)
print()

print(kramer(A.copy(), B.copy(), 5))
print(gauss(A.copy(), B.copy(), 5))
print(jordan_gauss(A.copy(), B.copy(), 5))
print(zadel(A.copy(), B.copy(), 2, 1000))
print(jacobi(A.copy(), B.copy(), 2, 1000))
