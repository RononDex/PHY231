# -*- coding: utf-8 -*-
# @Author: Elena Graverini
# @Date:   2015-06-27 13:34:57
# @Last Modified by:   Elena Graverini
# @Last Modified time: 2015-10-26 16:11:04

import math
import numpy as np
import scipy.stats as stats


def function_to_integrate(x, y):
    # Code here the function on which you want to try
    # the two integration methods.
    return math.exp(y-x)*np.sin(math.pi*x*y)**2.+np.sinh(x+y**2.)


def numerical_integration(func, domain, n):
    # Integrate a two-dimensional function numerically.
    # Inputs:
    # - "func": the function two integrate (it must be 2D)
    # - "domain": a tuple of the domain boundaries
    #             (xmin, xmax, ymin, ymax)
    # - n: the number of bins for each variable
    #      (you will have n*n bins at the end)
    # Outputs:
    # - the integral of the function
    xmin = domain[0]
    xmax = domain[1]
    ymin = domain[2]
    ymax = domain[3]
    dx = (xmax - xmin)/n
    dy = (ymax - ymin)/n
    x = np.linspace(xmin+dx*0.5,xmax-dx*0.5,n)
    y = np.linspace(ymin+dy*(0.5),ymax-dy*0.5,n)

    integral=0.
    for i in range(len(x)):
        for j in range(len(y)):
            integral += function_to_integrate(x[i],y[j])*dx*dy

    return integral


def montecarlo_integration(func, domain, n):
    # Integrate a two-dimensional function using the
    # "hit and miss" method.
    # Inputs:
    # - "func": the function two integrate (it must be 2D)
    # - "domain": a tuple of the volume boundaries
    #             (xmin, xmax, ymin, ymax, zmin, zmax)
    # - n: the number of random points to generate
    # Outputs:
    # - the integral of the function
    xmin = domain[0]
    xmax = domain[1]
    ymin = domain[2]
    ymax = domain[3]
    # you also need a third dimention to generate your
    # randoms: choose the boundaries wisely!
    zmin = domain[4]
    zmax = domain[5]


    x = xmin+(xmax-xmin)*stats.uniform.rvs(size=n)
    y = ymin+(ymax-ymin)*stats.uniform.rvs(size=n)
    z = zmin+(zmax-zmin)*stats.uniform.rvs(size=n)
    Vol=(xmax-xmin)*(ymax-ymin)*(zmax-zmin)
    r=0.
    for i in np.arange(0,n):
        f = function_to_integrate(x[i],y[i])
        if math.fabs(z[i]) <= math.fabs(f):
            if f>0 and z[i]>0:
                r += 1
            if f<0 and z[i]<0:
                r -= 1
    integral = Vol*r/n 
    return integral


# Choose the domain for the Monte Carlo integration
# (i.e. where you generate your random values)
# Replace the zeros with wisely chosen values!
#    "min/max of function in the area +/- 10% or 0.1"
my_zmin = -1.176
my_zmax = 3.787


if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python integration.py", and will not run when your
    # functions will be tested by us.
    # Example:
    print(numerical_integration(function_to_integrate, (-1., 1., -1., 1.), 100))
    print(montecarlo_integration(function_to_integrate, (-1., 1., -1., 1., my_zmin, my_zmax), 100))
    print(numerical_integration(function_to_integrate, (-1., 1., -1., 1.), 1000))
    print(montecarlo_integration(function_to_integrate, (-1., 1., -1., 1., my_zmin, my_zmax), 1000))
    pass
