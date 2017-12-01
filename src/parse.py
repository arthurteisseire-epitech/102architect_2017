#!/usr/bin/python3.6

import argparse
import sys
from matrix import *
from transformation import *

class add_to_list(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if 'arg' not in namespace:
            namespace.arg = []
        namespace.arg.append((self.dest, values))

def change_h_to_H():
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-h":
            sys.argv[i] = "-H"

def parse_all():
    parser = argparse.ArgumentParser()
    parser.add_argument("x", type=float, help="abscissa of the original point", nargs=1)
    parser.add_argument("y", type=float, help="ordinate of the original point", nargs=1)
    parser.add_argument("-t", type=float, help="translation along the coordinate vector (i, j)", action=add_to_list, nargs=2)
    parser.add_argument("-H", type=float, help="homothety with center O and scale factors m along x-axis and n along y-axis", action=add_to_list, nargs=2)
    parser.add_argument("-r", type=float, help="rotation centered in O at angle α degrees", action=add_to_list, nargs=1)
    parser.add_argument("-s", type=float, help="symmetry about the axis passing by O and inclined with an α-degree angle", action=add_to_list, nargs=1)
    args = parser.parse_args()
    return (args)

def print_infos(args):
    for arg in args.arg:
        if (arg[0] == 't'):
            print("Translation by the vector (%d, %d)" %(arg[1][0], arg[1][1]))
        elif (arg[0] == 'H'):
            print("Homothety by the ratios %d and %d" %(arg[1][0], arg[1][1]))
        elif (arg[0] == 'r'):
            print("Rotation at a %d degree angle" %(arg[1][0]))
        elif (arg[0] == 's'):
            print("Symmetry about an axis inclined with an angle of %d degrees" %(arg[1][0]))
        else:
            print("Wrong args")
            exit(84)
def gnn(nb):
    print("GNNNNN {}".format(nb))

def get_xres(args):
    is_first_arg = 1
    #print("ARGS:{}".format(args))
    for arg in args.arg:
        #print("ARG:{}".format(arg))
        if (arg[0] == 't'):
            f = translation
        elif (arg[0] == 'H'):
            f = homothethy
        elif (arg[0] == 'r'):
            print("SOY FELES")
            f = rotation
        elif (arg[0] == 's'):
            f = symmetry
        
        print("LEN:{} ARG:{} {}".format(len(arg[1]), arg[1][0] , arg[1][1]))
        if (len(arg[1]) == 1):
            arg_to_call = "arg[1][0]"
        else:
            arg_to_call = "arg[1][0], arg[1][1]"
        
        
        
        #print("ARG1:{} ARG2:{}".format(eval(arg_to_call)))
        if (is_first_arg == 1):
            xres = f(arg[1][0], arg[1][1])
            is_first_arg = 0
        else:
            xnew = f(arg[1][0], arg[1][1])
            xres = matrix_product(xres, xnew)
    return (xres)
