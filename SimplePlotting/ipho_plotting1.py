# -*- coding: utf-8 -*-
# @Author: Marco Tresch
# @Date:   2015-09-15
# @Last modified by:   Andreas Weiden
# @Last modified time: 2016-09-21 16:58:57
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt



def read_from_file(filename):
    # This function is kindly provided to you.
    # Thank the assistants! :)
    return np.loadtxt(filename, skiprows=1)


def histogramScore(distr):
    """
    Function that plots a histogram of the score the participants.
    Bins, limits and axis labels are to be adjusted in function body
    input: data array
    output: h, output from plt.hist
    f, pyplot figure
    """
    f = plt.figure()
    total_scores = [i[4] for i in distr]
    h = plt.hist(total_scores, 50, range=(0,50))
    plt.xlabel("totalscore")
    plt.ylabel("count")
    plt.ylim(0,14)
    plt.xlim(0, 50)
    return h, f


def scatterExperimentalTheoretical(distr):
    """
    Function that plots a 2D scatter plot of the experiment and theory score.
    Limits and axis labels are to be adjusted in function body
    input: data array
    output: s, output from plt.scatter
            f, pyplot figure
    """
    f = plt.figure()
    x = [i[2] for i in distr]
    y = [i[3] for i in distr]
    h = plt.scatter(x, y, s=20)
    plt.xlabel("experiment score")
    plt.ylabel("theory score")
    plt.xlim(0, 20)
    plt.ylim(0,30)
    return h, f


def annotateMedals(f, bins):
    # This function is kindly provided to you.
    # Thank the assistants! :)
    """
    Function to put annotations on an axis.
    Uses the five categories achievable at the IPhO, gold, silver, bronce,
    honorable mention and not mention.
    input: f, figure from plt.figure
           bins, binning used in the histogram (lowest edge, high edges, highest edge)
    output: None, modifies f
    """
    axes = f.gca()
    bin_centers = (bins[:-1] + bins[1:]) / 2
    medals = ("", "Honor", "Bronze", "Silber", "Gold")
    for medal, center in zip(medals, bin_centers):
        axes.annotate(medal, xy=(center, 0), va='top', ha='center',
                      xytext=(0, -11), textcoords='offset points')


def histogramMedals(distr):
    """
    Function that plots a histogram of the medals.
    Bins, limits and axis labels are to be adjusted in function body
    input: data array
    output: h, output from plt.hist
            f, pyplot figure
    """
    total_scores = [i[4] for i in distr]
    medals = []
    for score in total_scores:
        if score > 39.8:
            medals.append(5)
        elif score > 30.7:
            medals.append(4)
        elif score > 22.7:
            medals.append(3)
        elif score > 17.5:
            medals.append(2)
        else:
            medals.append(1)
            
    bins = np.array([0, 17.5, 22.7, 30.7, 39.8, 50])
    f = plt.figure()
    total_scores = [i[4] for i in distr]
    h = plt.hist(total_scores, bins = bins)
    plt.xlabel("medal")
    plt.ylabel("count")
    plt.xlim(0,50)
    plt.ylim(0,125)
    plt.gca().axes.get_xaxis().set_visible(False)

    annotateMedals(f, bins)
    return h, f


if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python plotting.py", and will not run when your
    # functions will be tested by us.
    # Example:
     data = read_from_file("ipho_markings.txt")    
     h, f = histogramScore(data)
     f.show()
     pass
