#!/usr/bin/python3.6
from matrix import *
#from transformation import *

A = [[2, -5, 1], [0, 3, 4], [-7, 1, 8]]
B = [[3, 2, 2], [-1, 3, 3], [2, 4, 4]]
print(A)
print(B)
C = matrix_product(A, B)
print(C)
