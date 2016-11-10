# -*- coding: utf-8 -*-
# @Author: Marco Tresch
# @Date:   2015-09-15
# @Last Modified by:   Marco Tresch
# @Last Modified time: 2015-09-15

import numpy as np
from  numpy import pi as pi
from  numpy import sqrt as sqrt
from  numpy import exp as exp
import matplotlib.pyplot as plt
from scipy.stats import norm


def read_from_file(filename):
    """
    input:  filename, string containing the filename
    output: numpy array of data
    """
    return np.loadtxt(filename)

def hist(dataSet):
    """
    Draw a histogram of the data
    input:  dataSet; one dimension
    output: h; return values from plt.hist
            f; figure from plt
    """
    iq = dataSet[:]
    f = plt.figure()
    h = plt.hist(iq,bins=110, range=(70.5,180.5))
     
    plt.title('IQ-distribution')
    plt.xlabel('IQ')
    plt.ylabel('number of people')
    plt.grid()
     
    u = iq.mean
    V = iq.std
    print("Mean :" + str(iq.mean()))
    print("Std. deviation : " + str(iq.std()))
     
    return h,f

def calculateProb(parameter, limit):
    """
    Calculates the probability for a distribution up to a limit
    input:  parameter; array of parameters for distribution (use the same order as scipy.stats function)
            limit; float number representing the limit
    output: probability; float number
    """
    return norm(parameter[0],parameter[1]).cdf(limit)

def findLimitForProb(parameter, probability):
    """
    Calculates the upper limit for a given probability
    input:  parameter; array of parameters for distribution (use the same order as scipy.stats function)
            probability; float number
    output: limit; upper limit, float number
    """
    return norm(parameter[0],parameter[1]).ppf(probability)

result = {
        "A": 0.0437954425215,
        "B": 0.182557681478,
        "C": 0.315128662427,
        "D": 101.125857745
            }    

if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "pythisthon trackProbability.py", and will not run when your
    # functions will be tested by us.
    # Example:
    # data = read_from_file("iq_data.txt")
    # (h,f)= hist(data)
    # f.show()

    data = read_from_file("iq_data.txt")
    (h,f) = hist(data)
    f.show()
    #parameter = dataSet
    limit = [90,115,120,140]
    parameter = [data.mean(),data.std()]
    print("Probability less than 90 = ", calculateProb(parameter, limit[0]))
    print("Probability more than 120 = ", 1 - calculateProb(parameter, limit[2]))
    print("Probability between 115 and 140 = ", calculateProb(parameter, limit[3])-  calculateProb(parameter, limit[1]))     
 
 
    #print "Probability = ", calculateProb(parameter, 115) - calculateProb(parameter, 140)
    probability = 0.23   
    print("highest IQ of a percentage =", findLimitForProb(parameter, probability))
    # (h,f)= hist(data)
    # f.show()

    pass
