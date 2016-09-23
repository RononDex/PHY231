# -*- coding: utf-8 -*-
# @Author: Marco Tresch
# @Date:   2015-09-15
# @Last modified by:   Andreas Weiden
# @Last modified time: 2016-09-21 16:10:17
import numpy as np
import matplotlib.pyplot as plt


def read_from_file(filename):
    # This function is kindly provided to you.
    # Thank the assistants!  :)
    return np.loadtxt(filename, skiprows=1)


def getCountriesMean(data):
    """
    Function that calculates the mean score for each country.
    input: data array
    output: data array (sorted)
    """
    
    means = []
    
    country = [i[1] for i in data]
    total_scores = [i[4] for i in data]

    curCountry = 0
    curTotal = 0
    countryCount = 0
    

    for i in range(0, len(country)):
        if (country[i] != curCountry):
            if countryCount > 0:
                means.append( curTotal / countryCount)
            curCountry = country[i]
            curTotal = 0
            countryCount = 0
        
        curTotal += total_scores[i]
        countryCount += 1
    means.sort()
    return means


def plotCountriesMean(distr):
    """
    Function that plots a histogram of the mean score of each country.
    Bins, limits and axis labels are to be adjusted in function body
    input: data array
    output: p, output from plt.plot
            f, pyplot figure
    """
    data = getCountriesMean(distr)
    f = plt.figure()
    h = plt.hist(data, 20)
    plt.xlabel("totalscore")
    plt.ylabel("count")
    plt.ylim(0,10)
    plt.xlim(0, 84)
    return h, f


if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python plotting.py", and will not run when your
    # functions will be tested by us.
    # Example:
    data = read_from_file("ipho_markings.txt")
    p, f = plotCountriesMean(data)
    f.show()
    pass
