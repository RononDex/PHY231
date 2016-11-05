# -*- coding: utf-8 -*-
# @Author: Marco Tresch
# @Date:   2015-09-15
# @Last Modified by:   Marco Tresch
# @Last Modified time: 2015-09-15
import numpy as np
import matplotlib.pyplot as plt
import scipy.stats as stats

def convolute_plot(lam, mu, sigma, nEntries, randomState=None):
    """
    This function produces a data_set from a convoluted function (Exponential + Gaussian)
    input:  lambda, decay rate
            mu, parameter of gaussian PDF
            sigma, parameter of gaussian PDF
            nEntries_Final, number of data points in data_set
            randomState, starting value for Rangom generation, see scipy doc
    output: data_set, array containing data points from convolution
    """
    np.random.seed(randomState) # to have the same starting point
    data_set = []
    return data_set

if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python convolution.py", and will not run when your
    # functions will be tested by us.
    pass
