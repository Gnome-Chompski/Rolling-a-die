# -*- coding: utf-8 -*-
"""
Created on Mon May  8 10:22:25 2017

@author: Dante

Program determines the longest run of the same number with a sequence of random dice rolls.

eg. 13222421 the longest run would be three
    12331215 the longest run would be two
    
The runs are randomly generated and presented within a histogram of ten bins. The size of the die
can be defined using the class die. makeHistogram generates the histogram which illustrates which 
run of numbers was the longest and how often it occured.
getAverage takes in three parameters the size of the die, how long the randomly generated sequence is and
how many times the experiment should be repeated. The function plots the longest run in the sequence
against how often it has occurred and produces the average of the whole run.

For example: a die that can only roll 1, in a sequence of length 10 repeated 1000 times will average 10.
It will produce a run of 1111111111, 1000 times. Sample case shown at end of code.
"""

import random, pylab

def getMeanAndStd(X):
    """
      - X, a list of integers
      - returns the mean and standard deviation
    """
    mean = sum(X)/float(len(X))
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    std = (tot/len(X))**0.5
    return mean, std

class Die(object):
    def __init__(self, valList):
        """ 
        valList, a list containing the possible numbers the die can roll 
        """
        self.possibleVals = valList[:]
    def roll(self):
        return random.choice(self.possibleVals)

def makeHistogram(values, numBins, xLabel, yLabel, title=None):
    """
      - values, a sequence of numbers
      - numBins, a positive int
      - xLabel, yLabel, title, are strings
      - Produces a histogram of values with numBins bins and the indicated labels
        for the x and y axis
      - If title is provided by caller, puts that title on the figure and otherwise
        does not title the figure
    """
    
    pylab.hist(values, numBins)
    pylab.xlabel(xLabel)
    pylab.ylabel(yLabel)
    if title != None:
        pylab.title(title)
    pylab.show()
    
                    
def getAverage(die, numRolls, numTrials):
    """
      - die, a Die
      - numRolls, numTrials, are positive ints
      - Calculates the expected mean value of the longest run of a number
        over numTrials runs of numRolls rolls.
      - Calls makeHistogram to produce a histogram of the longest runs for all
        the trials. There should be 10 bins in the histogram
      - Choose appropriate labels for the x and y axes.
      - Returns the mean calculated
    """
    results = []
    for i in range(numTrials):
        rollsec = []
        counter = 1
        bestrolls = [1]
        for j in range(numRolls):
            rollsec.append(die.roll())
            if len(rollsec) == 2 and rollsec[0] == rollsec[1]:
                counter += 1
                rollsec.remove(rollsec[0])
                if j == (numRolls -1):
                    bestrolls.append(counter)
            elif len(rollsec) == 2 and rollsec[0] != rollsec[1]:
                bestrolls.append(counter)
                counter = 1
                rollsec.remove(rollsec[0])
        results.append(max(bestrolls))
        
    makeHistogram(results, 10, "Longest Runs", "No. of Occurrences")
        
    return round(getMeanAndStd(results)[0],3)
                
            
#print(getAverage(Die([1,2,3,4,5,6]), 500, 10000))
print(getAverage(Die([1]), 10, 1000))

























