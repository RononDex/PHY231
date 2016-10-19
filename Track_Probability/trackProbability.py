# -*- coding: utf-8 -*-
# @Author: Marco Tresch
# @Date:   2015-09-15
# @Last Modified by:   Elena Graverini
# @Last Modified time: 2016-10-13 12:02:51

# Align the behaviour of python2 and python3
# with integer divisions
from __future__ import division


def probabilityTrack(nHits, nLayers, efficiency):
    """
    calculate the probability that a track is reconstructed, given a minimum number of fired layers, and the total number of layers of the tracking detector
    """
    probability = 0.
    return probability


def probabilityMultipleTracks(nHits, nLayers, efficiency, nTracks):
    """
    calculate the probability for multiple tracks
    """
    probability = 0.
    return probability

resultA = {
    "atLeast4": 0,
    "atLeast5": 0,
    "atLeast6": 0
}
resultB = {
    "atLeast4": 0,
    "atLeast5": 0,
    "atLeast6": 0
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
    pass
