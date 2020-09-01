# -*- coding: utf-8 -*-
"""
Created on Sat Jul  4 00:33:08 2020

@author: lars-johan.brannmark
"""
import sys
import numpy as np
import matplotlib.pyplot as plt

class Heaviside(object):
    
    def __init__(self, eps=None):
        self.eps = eps
        
    def __call__(self, x):
        eps = self.eps
        x = np.array(x)
        if not eps:
            val = 1.0*(x >= 0)
        else:
            val = np.zeros_like(x)
            val = np.where(np.logical_and(-eps <= x, x <= eps),
                           0.5 + x/(2.0*eps) + 1/(2*np.pi)*np.sin(np.pi*x/eps), val)
            val = np.where(eps < x, 1, val)
        return val

    def plot(self, xmin, xmax):
        eps = self.eps
        if eps:
            x_eps = np.linspace(-eps, eps, 201)
            x_neg = np.array([min(xmin,-eps), -eps])
            x_pos = np.array([eps, max(eps,xmax)])
            x = np.concatenate((x_neg, x_eps, x_pos))
            y = self(x)
        else:
            if xmin < 0 <= xmax:
                x = np.array([xmin, 0, 0, xmax])
                y = np.array([0, 0, 1, 1])
            else:
                x = np.array([xmin, xmax])
                y = self(x)
        plt.figure()
        plt.plot(x, y)
        plt.axis([xmin, xmax, -0.1, 1.1])
        plt.title('H(x)')
        plt.xlabel('x')
        plt.ylabel('y = H(x)')
        plt.show()

def test_Heaviside():
    H1 = Heaviside()
    H2 = Heaviside(0.1)
    H1.plot(-1, 1)
    H2.plot(-1, 1)
    success = H1(-1) == 0 and H1(0) == 1 and H1(1) ==1 and \
    H2(-1) == 0 and H2(0) == 0.5 and H2(1) == 1
    msg = 'Error in class Heaviside'
    assert success, msg
    
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == 'test':
        test_Heaviside()