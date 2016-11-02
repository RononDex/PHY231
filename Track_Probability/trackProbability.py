# -*- coding: utf-8 -*-
# @Author: Marco Tresch
# @Date:   2015-09-15
# @Last Modified by:   Elena Graverini
# @Last Modified time: 2016-10-13 12:02:51

# Align the behaviour of python2 and python3
# with integer divisions
from __future__ import division
import math


def probabilityTrack(nHits, nLayers, efficiency):
    """
    calculate the probability that a track is reconstructed, given a minimum number of fired layers, and the total number of layers of the tracking detector
    """
    n = math.factorial(nLayers)
    sum = 0
    
    for k in range(nHits,nLayers+1):
        i = math.factorial(k)
        n_k = math.factorial(nLayers-k)
        value1 = (n/(i*n_k))*efficiency**k
        value2 = value1*(1-efficiency)**(nLayers-k)
        sum += value2
        k += 1
          
    probability = sum
    return probability


def probabilityMultipleTracks(nHits, nLayers, efficiency, nTracks):
    """
    calculate the probability for multiple tracks
    """
    probability = probabilityTrack(nHits, nLayers, efficiency) ** nTracks
    return probability

resultA = {
        "atLeast4":probabilityTrack(4,6,0.9),
        "atLeast5":probabilityTrack(5,6,0.9),
        "atLeast6":probabilityTrack(6,6,0.9)
        }
resultB = {
        "atLeast4":probabilityMultipleTracks(4,6,0.9,4),
        "atLeast5":probabilityMultipleTracks(5,6,0.9,4),
        "atLeast6":probabilityMultipleTracks(6,6,0.9,4)
        }


if __name__ == '__main__':
    # You can use the "main" to test your code.
    # Code that follows the "if __name__ == '__main__':" snippet
    # is only executed when you execute this script with
    # "python trackProbability.py", and will not run when your
    # functions will be tested by us.
    # Example:
    #nHits = 4
    #nLayers = 6
    #efficiency = 0.9
    #prob_one_track = probabilityTrack(nHits,nLayers,efficiency)
    # print prob_one_track
    print(resultA)
    print(resultB)
    pass
