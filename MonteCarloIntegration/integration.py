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
    return 0.


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
    integral = 0.  # compute your integral here
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
    integral = 0.  # compute your integral here
    return integral


# Choose the domain for the Monte Carlo integration
# (i.e. where you generate your random values)
# Replace the zeros with wisely chosen values!
my_zmin = 0.
my_zmax = 0.


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
    pass
