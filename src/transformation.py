from math import *
def translation(i, j):
    T = [[1, 0, i],\
        [0, 1, j],\
        [0, 0, 1]]
    return(T)

def homothethy(i, j):
    H = [[i, 0, 0],\
        [0, j, 0],\
        [0, 0, 1]]
    return(H)

def rotation(a):
    ca = cos(radians(a))
    sa = sin(radians(a))
    R = [[ca, sa, 0],\
        [sa, ca, 0],\
        [0, 0, 1]]
    return(R)

def symmetry(a):
    Sox = [[0, 0, 0],\
        [0, 0, 0],\
        [0, 0, 1]]
    S = matrix_product(rotation(-a), matrix_product(Sox, rotation(a)))
    return(S)

