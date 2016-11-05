# -*- coding: utf-8 -*-
# @Author: Elena Graverini
# @Date:   2015-06-27 13:34:57
# @Last Modified by:   Elena Graverini
# @Last Modified time: 2015-10-26 16:11:04

import math
import numpy as np
import scipy.stats as stats


def function_to_integrate(x, y):
    toRet = np.exp(y-x)*((np.sin(np.pi * x * y))**2) + np.sinh(x + y*y)
    return toRet


def numerical_integration(func, domain, n):
    n = n
    
    # Integrate a two-dimensional function numerically.
    # Inputs:
    # - "func": the function two integrate (it must be 2D)
    # - "domain": a tuple of the domain boundaries
    #             (xmin, xmax, ymin, ymax)
    # - n: the number of bins for each variable
    #      (you will have n*n bins at the end)
    # Outputs:
    # - the integral of the function
    print domain
    print n
    n = int(n)
    print n
    xmin = float(domain[0])
    xmax = float(domain[1])
    ymin = float(domain[2])
    ymax = float(domain[3])
    xbinsize = ((xmax-xmin)/float(n))
    ybinsize = ((ymax-ymin)/float(n))
    xcentres = np.array([(xbinsize/2)+ xmin + xbinsize * float(i) for i in range(n)])
    ycentres = np.array([(ybinsize/2)+ ymin + ybinsize * float(i) for i in range(n)])
    integral = 0.  # compute your integral here
    for x in xcentres:
        for y in ycentres:
            integral += func(x,y)
    integral = integral * xbinsize * ybinsize
    print integral
    return integral


def montecarlo_integration(func, domain, n):
    n = n
    # Integrate a two-dimensional function using the
    # "hit and miss" method.
    # Inputs:
    # - "func": the function two integrate (it must be 2D)
    # - "domain": a tuple of the volume boundaries
    #             (xmin, xmax, ymin, ymax, zmin, zmax)
    # - n: the number of random poinpointsts to generate
    # Outputs:
    # - the integral of the function
    print domain
    print n
    n = int(n)
    print n
    
    xmin = float(domain[0])
    xmax = float(domain[1])
    ymin = float(domain[2])
    ymax = float(domain[3])
    # you also need a third dimention to generate your
    # randoms: choose the boundaries wisely!
    zmin = float(domain[4])
    zmax = float(domain[5])
    counted = 0
    for i in range(n):
        x = xmin + np.random.rand()*(xmax-xmin)
        y = ymin + np.random.rand()*(ymax-ymin)
        z = zmin + np.random.rand()*(zmax-zmin)
        funcval = func(x,y)
        if (z >= 0 and z<funcval):
            counted += 1
        elif (z<=0 and z>funcval):
            counted -= 1
    counted = float(counted)
    n = float(n)
    integral = ((zmax-zmin)*((xmax-xmin)*(ymax-ymin)*counted/n))  # compute your integral here
    print integral
    return integral


# Choose the domain for the Monte Carlo integration
# (i.e. where you generate your random values)
# Replace the zeros with wisely chosen values!
#my_zmin = -3.
#my_zmax = 7.


my_zmin = -1.176 
my_zmax = 3.787

if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python integration.py", and will not run when your
    # functions will be tested by us.
    # Example:
    # print numerical_integration(function_to_integrate, (-1., 1., -1., 1.), 100)
    # print montecarlo_integration(function_to_integrate, (-1., 1., -1., 1., my_zmin, my_zmax), 100)
    # print numerical_integration(function_to_integrate, (-1., 1., -1., 1.), 1000)
    # print montecarlo_integration(function_to_integrate, (-1., 1., -1., 1., my_zmin, my_zmax), 1000)
    for i in range(6):
        print 'monte:', montecarlo_integration(function_to_integrate, [-1.,1.,-1.,1., -3.,7.],10**i)
        print 'numerical:', numerical_integration(function_to_integrate, [-1.,1.,-1.,1.],int(np.sqrt(10**i)))
    
    pass
