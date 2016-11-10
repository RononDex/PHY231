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
     
    xb = np.arange(-30,500000, 5000)
    xp = np.arange(-30,30,0.2)
    
    # Plot the exponential curve
    plt.figure()
    plt.subplot(3,1,1)
    xf = stats.expon(0.,1./lam).rvs(nEntries)
    plt.hist(xf,xb, normed=True)
    plt.plot(xb, stats.expon(0,1./lam).pdf(xb))
     
    # Plot the gaussian distribution
    plt.subplot(3,1,2)   
    xg = stats.norm(mu, sigma).rvs(nEntries)
    plt.hist(xg,xp, normed=True)
    plt.plot(xp,stats.norm(mu,sigma).pdf(xp))
     
    # Plot the convolution of the two distributions
    plt.subplot(3,1,3)
    plt.hist(xf+xg,xb,normed=True)
    plt.plot(xb, stats.expon(0,1./lam).pdf(xb))
         
    data_set = xf+xg
    return data_set


if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python convolution.py", and will not run when your
    # functions will be tested by us.

    lam = 1./150000
    mu = 0
    sigma = 10.
    n = 100000
    #parameter = [mu,sigma]
    solution = convolute_plot(lam, mu, sigma, n, randomState=876765764)
    print(solution)
    pass
