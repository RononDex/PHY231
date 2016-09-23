# -*- coding: utf-8 -*-
# @Author: Marco Tresch 
# @Date:   2015-09-15
# @Last Modified by:   Marco Tresch
# @Last Modified time: 2015-09-15
import numpy as np
import matplotlib.pyplot as plt

def produceData():
    # This function is kindly provided to you.
    # Thank the assistants! :)
    data = np.random.normal(loc=0.0, scale=1.0, size=10000)
    return data

def produceData2D(mean=[0,0], cov=[[1,10],[-10,100]]):
    # This function is kindly provided to you.
    # Thank the assistants! :)
    data = np.random.multivariate_normal(mean,cov,5000)
    return data

def histogram(distr):
    """
    Function that plots a histogram of a distribution.
    Bins and axis labels are to adjust in function body
    input: data array
    output: h, output from plt.hist
            f, pyplot figure
    """
    f = plt.figure()
    h = plt.hist(distr, 20, normed=1, histtype='stepfilled')
    plt.xlabel("test")
    plt.ylabel("test")
    return h, f

def scatter(distr):
    """
    Function producing a scatter plot of a given dataset
    input: 2-D data set
    output: h, output from plt.scatter
            f, pyplot figure
    """
    x = [i[0] for i in distr]
    y = [i[1] for i in distr]
    f = plt.figure()
    h = plt.scatter(x, y, s=20)
    plt.xlabel("")
    plt.ylabel("test")

    return h,f

if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python plotting.py", and will not run when your
    # functions will be tested by us.
    # Example:
    data = produceData()
    (h,f) = histogram(data)
    f.show()
    data_scatter = produceData2D()
    (sh,sf) = scatter(data_scatter)
    sf.show()
    pass
