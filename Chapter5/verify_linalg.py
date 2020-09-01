# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 22:16:15 2020

@author: lars-johan.brannmark
"""

import numpy as np

def test_addition():
    n = 4  # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))    
    tol = 1E-14
    result1 = A + B
    result2 = B + A
    assert abs(result1 - result2).max() < tol
    
def test_distributive():
    n = 4  # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))  
    C = np.matrix(np.random.rand(n, n))  
    tol = 1E-14
    result1 = (A + B)*C
    result2 = A*C + B*C
    assert abs(result1 - result2).max() < tol
    
def test_associative():
    n = 4  # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))  
    C = np.matrix(np.random.rand(n, n))  
    tol = 1E-14
    result1 = (A*B) * C
    result2 = A * (B*C)
    assert abs(result1 - result2).max() < tol
    
def test_rank():
    n = 4  # matrix size
    A = np.matrix(np.random.rand(n, n))
    tol = 1E-14
    result1 = np.linalg.matrix_rank(A)
    result2 = np.linalg.matrix_rank(A.T)
    assert result1 == result2
    
def test_det():
    n = 4  # matrix size
    A = np.matrix(np.random.rand(n, n))
    B = np.matrix(np.random.rand(n, n))    
    tol = 1E-14
    result1 = np.linalg.det(A*B)
    result2 = np.linalg.det(A)*np.linalg.det(B)
    assert abs(result1 - result2) < tol
    
def test_eigenvalues():
    n = 4  # matrix size
    A = np.matrix(np.random.rand(n, n))
    tol = 1E-14
    result1 = np.linalg.eigvals(A)
    result2 = np.linalg.eigvals(A.T)
    assert abs(result1 - result2).max() < tol
    
test_addition()
test_distributive()
test_associative()
test_rank()
test_det()
test_eigenvalues()



