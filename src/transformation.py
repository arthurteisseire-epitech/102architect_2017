from math import *
def translation(i, j):
    T = [[1, 0, i],\
        [O, 1, j],\
        [0, 0, 1]]

def homothethy(i, j):
    H = [[i, 0, 0],\
        [0, j, 0],\
        [0, 0, 1]]

def rotation(a):
    ca = cos(radians(a))
    sa = sin(radians(a))
    R = [[ca, sa, 0],\
        [sa, ca, 0],\
        [0, 0, 1]]

def symmetry(a):
    S = [[0, 0, 0],\
        [0, 0, 0],\
        [0, 0, 1]]

