# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 21:38:32 2020

@author: lars-johan.brannmark
"""

# Exercise 7.35 d): 
# >> run optimization.py [2,1,100] [5,3,80] [0,4,150] [1,0,0] [0,1,0]

# Exercise 7.35 e) and g): 
# >> run optimization.py [2,1,100] [5,3,80] [0,4,150] [1,0,0] [0,1,0] 45 14

import sys
import numpy as np
import matplotlib.pyplot as plt

# 7.35 d) and g)
if 5 < len(sys.argv):
    plt.figure()
    A = np.zeros((5,2))
    B = np.zeros((5,1))
    for i in range(1,6):
        a, b, c = eval(sys.argv[i])
        A[i-1,0] = a
        A[i-1,1] = b
        B[i-1] = c
        if a != 0 and b != 0:
            x_start = 0.0
            x_stop = c/float(a)
            y_start = c/float(b)
            y_stop = 0
        if a == 0:
            x_start = 0
            x_stop = 100
            y_start = c/float(b)
            y_stop = y_start
        if b == 0:
            x_start = c/float(a)
            x_stop = x_start
            y_start = 0
            y_stop = 100
        plt.plot([x_start, x_stop],[y_start, y_stop], lw=2.0)
        plt.show()
        
        #7.35 g) Find the corners of the solution set T by solving the
        #constrint equations pairwise, to find the intersection of lines. Then
        #check which intersection points fulfill all of the constraints.
        corners = []
        for i in range(0,5):
            for j in range(i+1,5):
                try:
                    x = np.linalg.solve(A[[i,j],:],B[[i,j]])
                    y = A.dot(x)
                except:
                    continue
                if (y[0:3] <= B[0:3] + 1e-10).all() and (y[3:] + 1e-10 >= B[3:]).all():
                    corners.append(x)

#7.35 e)
if 6 < len(sys.argv) < 9:
    p = eval(sys.argv[6])
    q = eval(sys.argv[7])
    f = lambda x, y: p*x + q*y
    alpha_list = range(20, 721, 100)
    for alpha in alpha_list:
        x_start = 0
        x_stop = alpha/float(p)
        y_start = alpha/float(q)
        y_stop = 0
        plt.plot([x_start, x_stop],[y_start, y_stop], '--', label='f(x,y)=%s'%alpha)
        plt.legend()
        plt.show()
    fmax = 0
    solution = {}
    for i, c in enumerate(corners):
        fval = f(float(c[0]),float(c[1]))
        print fval
        if fval > fmax:
            fmax = fval
            solution['x_opt'] = float(corners[i][0])
            solution['y_opt'] = float(corners[i][1])
            solution['f_opt'] = fval
    print solution
        
        
        

            
