#!/usr/bin/python3.6

import argparse
import sys

class put_in_order(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        if 'args' not in namespace:
            namespace.args = []
        namespace.args.append((self.dest, values))

def change_h_to_H():
    for i in range(len(sys.argv)):
        if sys.argv[i] == "-h":
            sys.argv[i] = "-H"

def parse_all():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", type=float, help="translation along the coordinate vector (i, j)", action=put_in_order, nargs=2)
    parser.add_argument("-H", type=float, help="homothety with center 0 and scale factors m along x-axis and n along y-axis", action=put_in_order, nargs=2)
    parser.add_argument("-r", type=float, help="rotation centered in O at angle α degrees", action=put_in_order, nargs=1)
    parser.add_argument("-s", type=float, help="symmetry about the axis passing by 0 and inclined with an α-degree angle", action=put_in_order, nargs=1)
    args = parser.parse_args()
    return (args)

def compute_args(args):
    for arg in args.H:
        print(arg)

change_h_to_H()
args = parse_all()
print(args)
#compute_args(args)
