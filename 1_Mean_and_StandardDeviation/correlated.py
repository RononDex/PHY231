#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Elena Graverini
# @Date:   2015-07-05 22:03:20
# @Last Modified by:   Elena Graverini
# @Last Modified time: 2015-07-05 22:19:35

import math


def compute_n2(n1, theta1, theta2):
    # Compute the refraction index as of exercise 1.

    # n1 * sin(theta1) = n2 * sin(theta2)
    # ==> n2 = (n1 * sin(theta1)) / sin(theta2)
    n2 = (n1 * math.sin(theta1)) / math.sin(theta2)
    return n2


def compute_n2_uncertainty(n1, theta1, theta2, n1_error, theta1_error, theta2_error, rho):
    # Compute the uncertainty on n2 as of exercise 2.

    # n1 * sin(theta1) = n2 * sin(theta2)
    
    n2_error = 0.
    return n2_error


# Decide what correlation coefficient makes sense for theta1 and theta2
# and compute n2 as of exercise 3.
# Store the result in this dictionary.
# Change the zeros into function calls to compute your numbers!
results = {
    'my_rho'           : 0.,
    'my_n2'            : 1.16956991625651,
    'my_n2_uncertainty': 0.
}

if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python correlated.py", and will not run when your
    # functions will be tested by us.
    # Example:
    # for key in results:
    #     print key, 'is', results[key]
    print(compute_n2(1.001, 46 / 360 * 2 * math.pi, 38 / 360 * 2 * math.pi))
    pass
