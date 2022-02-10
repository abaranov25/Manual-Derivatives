#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 25 19:33:14 2021

@author: Allen Baranov

Goal: To write a predicting function that iterates and uses predicted points to predict future points
"""

import numpy as np
from math import comb as nCr
from math import factorial
import matplotlib.pyplot as plt

class ManualDerivatives:
    
    h = 0.001
    iv = []
    ov = []
    
    def __init__(self,iv,ov):
        """

        Args:
            iv (numpy ndarray): evenly spaced x-values of points (input values)
            ov (numpy ndarray): y-values of points
            h (float): difference in consecutive x-values
        """
        self.iv = iv
        self.ov = ov
        self.h = iv[1]-iv[0]
    
    def get_iv(self):
        return self.iv
    
    def get_ov(self):
        return self.ov
    
    def get_h(self):
        return self.h

### Helper functions ###

"""
nth_derivative

Computes the approximate nth derivative of a function at a given input 
point. 

Args:
    n (integer): Which derivative is to be taken
    x0 (float): the value at which the nth derivative is being calculated
        
Output:
    A float value corresponding to the nth derivative at that point
"""

def nth_derivative(thisFunction, n, x0):
    iv = thisFunction.get_iv()
    ov = thisFunction.get_ov()
    h = thisFunction.get_h()
    s = 0
    
    for k in range(n+1):
        i = iv.index(round(x0 + k*h, 10))
        s += (-1)**(n-k) * nCr(n,k) * ov[i]

    return (1/h) ** n * s

"""
taylor_approx

Computes an approximation of a function based on the Taylor series, using the approximations
provided by nth_derivative.

Args:
    m (integer): The degree of the Taylor approximation
    x0 (float): the value at which the approximation is centered
    x (float): the value which will be approximated
    
Output:
    A float value corresponding to the approximation of the function at that point

"""

def taylor_approx(thisFunction, m, x0, x):
    iv = thisFunction.get_iv()
    ov = thisFunction.get_ov()
    h = thisFunction.get_h()
    s = 0
    
    for n in range(m+1):
        s += nth_derivative(thisFunction, n, x0) * ((x-x0) ** n) / factorial(n)
        
    return s


"""
plot_func

Plots a graph of the taylor approximation at all points and all points provided by (iv,ov). 

Args:
    m (float): The minimum value of the graph inputs
    M (float): The maximum value of the graph inputs
    d (float): The distance between consecutive points to plot
    n (int): The degree of the Taylor approximation
    
Output:
    A matplotlib plot of the function as estimated by the helper functions
    
"""

def plot_func(thisFunction, m, M, d, n):
    iv = thisFunction.get_iv()
    ov = thisFunction.get_ov()
    h = thisFunction.get_h()
    
    l = round((M - m) / d)
    x = []
    y = []
    for i in range(l):
        x.append(m + d*i)
        y.append(taylor_approx(thisFunction, n, m, m + d*i))

    
    fig = plt.figure()
    plt.plot(iv, ov, 'ro')
    plt.plot(x,y, 'b-')
    plt.xlabel('Input')
    plt.ylabel('Output')
    
    plt.show()    