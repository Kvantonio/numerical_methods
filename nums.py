import numpy as np
import copy

from gauss import gauss
from kramer import kramer
from zadel import zadel

import random

def generate_rand(l, rd):
    A=[]
    for _ in range(l):
        A.append([random.random() for _ in range(l)])

    B = [random.random() for _ in range(l)]

    return(A,B)


A=[
    [2,1,1],
    [1,-1,0],
    [3,-1,2]
  ]

B = [2,-2,2]



A, B= generate_rand(6,2)

print(kramer(A, B, 5))
print(gauss(A, B, 5))
print(zadel(A, B, 5))






