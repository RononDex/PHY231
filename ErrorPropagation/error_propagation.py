# -*- coding: utf-8 -*-
# @Author: Elena Graverini
# @Date:   2015-06-27 13:34:57
# @Last Modified by:   Elena Graverini
# @Last Modified time: 2015-07-05 20:17:35

import math

def compute_diameter(volume):
    # Given the volume of a sphere,
    # compute its diameter.
    
    # V = 4 / 3 * pi * r^3   ==>  d = 2 * ( 3 * V / ( 4 * pi))^1/3
    diameter = (6*volume/math.pi)**(1./3)
    return diameter

def compute_max_uncertainty(volume, max_volume_err):
    # Given the volume of a sphere, and the
    # maximum allowed uncertainty on it,
    # return the maximum allowed uncertainty 
    # on the diameter of the sphere.

    # First we derive the fomula in respect to the diameter "d"
    dd = compute_diameter(volume)/(3*volume)
    
    # The absolute error is then given by the relative error * derivative
    max_uncertainty = max_volume_err*dd
    return max_uncertainty


if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python error_propagation.py", and will not run when your
    # functions will be tested by us.
    # Example:
    # print compute_max_uncertainty(5., 3.)
    pass
