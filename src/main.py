#!/usr/bin/python3.6
from matrix import *
from transformation import *
from parse import *

try:
    change_h_to_H()
    args = parse_all()
    print_infos(args)
    args.arg = list(reversed(args.arg))
    xpos = coord_to_matrix(args.x, args.y)
    xres = get_xres(args)
    print("NGNGNGNGNG")
    print(xres, matrix_product(xpos, xres))
except:
    print("Need at least x y args and one transformation")
    exit(84)

