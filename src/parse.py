#!/usr/bin/python3.6

import argparse
import sys

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

try:
    change_h_to_H()
    args = parse_all()
    #print(args.x)
    #print(args.y)
    print_infos(args)
except:
    print("Need at least x y args and one transformation")
    exit(84)
