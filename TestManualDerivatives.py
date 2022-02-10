#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 00:46:38 2022

@author: allenbaranov
"""

import ManualDerivatives as MD
import math
from math import sin
import matplotlib.pyplot as plt

"""
Test of manual derivatives

A function is provided in f(x) below, then inputs are 

"""


def f(x):
    
    return math.exp(-(x/10)**2)
    
    #return 2*x - 3*math.sin(x) + math.cos(x)


def run_test0():
    h = .5 # How close to a real derivative this becomes
    x0 = -20 # Look at points around this value
    x = -10 # Predict points around this value
    n = 5 # How many taylor terms to use
    
    ub = x0 + n*h # Upper bound of values used for function
    l = round((x - x0) / h) # Length of arrays containing inputs and outputs
    dist = round((x - ub) / h, 10) # Distance between examined value and upper bound, in terms of h
    
    
    iv = []
    for i in range(n+1):
        iv.append(round(x0 + i*h,10))
    
    ov = []
    for i in range(len(iv)):
        ov.append(f(iv[i]))
    
    
    case = MD.ManualDerivatives(iv,ov) # Instance of manual derivative class
    pred = MD.taylor_approx(case, n, x0, x) # Estimated y-value
    error = round(abs((pred - f(x)) / pred) * 100, 3)
    
    
    MD.plot_func(case, x0, x, .001, n)
    print("Value " + str(x) + " is " + str(dist) + "h away from highest value " + str(ub) + " with h=" + str(h))
    print("Error: " + str(error) + "%")

def run_test1():
    x0 = 1
    x = 10
    n = 13
    
    cases_per_day = [1512, 1622, 1729, 1729, 1729, 2130, 2275, 2321, 2471, 2590, 2590, 2590, 3008, 3194]
    days_since_dec = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
    
    case = MD.ManualDerivatives(days_since_dec, cases_per_day)
    MD.plot_func(case, x0, x, 0.25, n)
    
run_test0()
#run_test1()




