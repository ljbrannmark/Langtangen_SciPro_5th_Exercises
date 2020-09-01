# -*- coding: utf-8 -*-
"""
Created on Sun Dec  8 22:57:01 2019

@author: lars-johan.brannmark
"""

import argparse
from sinesum2 import table
from math import *

def myeval(str):
    return eval(str)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--n',type=int,default=[30],dest='n',
                        metavar='n',nargs='*',
                        help='A list of integers.')
    parser.add_argument('--alpha',type=float,default=[0.2],dest='alpha',
                        metavar='alpha',nargs='*',
                        help='A list of alpha values.')
    parser.add_argument('--T',type=myeval,default=2*pi,dest='T',
                        metavar='T',
                        help='A real number.')

    args=parser.parse_args()
    table(args.n, args.alpha, args.T)