#! /usr/bin/env python3

import scipy
import matplotlib.pyplot as plt

p = 0.5
n = 300
k = 200
victory = 10;
ruin = 0;
interval = victory - ruin + 1

winLose = 2*( scipy.random.random((n,k,interval)) <= p ) - 1
totals = scipy.cumsum(winLose, axis = 0)

start = scipy.multiply.outer( scipy.ones((n+1,k), dtype=int), scipy.arange(ruin, victory+1, dtype=int))
paths = scipy.zeros((n+1,k,interval), dtype=int)
paths[ 1:n+1, :,:] = totals
paths = paths + start

def match(a,b,nomatch=None):
    return  b.index(a) if a in b else nomatch
# arguments: a is a scalar, b is a python list, value of nomatch is scalar
# returns the position of first match of its first argument in its second argument
# but if a is not there, returns the value nomatch
# modeled on the R function "match", but with less generality

hitVictory = scipy.apply_along_axis(lambda x:( match(victory,x.tolist(),nomatch=n+2)), 0, paths)
hitRuin = scipy.apply_along_axis(lambda x:match(ruin,x.tolist(),nomatch=n+2), 0, paths)
# If no ruin or victory on a walk, nomatch=n+2 sets the hitting
# time to be two more than the number of steps, one more than
# the column length.
durationUntilRuinOrVictory = scipy.minimum(hitVictory, hitRuin)

import numpy.ma
durationMasked = scipy.ma.masked_greater(durationUntilRuinOrVictory, n)

startValues = scipy.arange(ruin, victory+1, dtype=int)
meanDuration = scipy.mean(durationUntilRuinOrVictory, axis = 0)
durationFunction = scipy.polyfit( startValues, meanDuration, 2)
print( "Duration function is: ", durationFunction[2], "+", durationFunction[1], "x+", durationFunction[0], "x^2") 
# should return coefficients to (x-ruin)*(victory - x), descending degree order

plt.scatter(startValues, meanDuration)
X = scipy.linspace(ruin, victory, 256, endpoint=True)
Y = durationFunction[2] + durationFunction[1]*X + durationFunction[0]*X**2
plt.plot(X,Y)
plt.show()

## NAME: duration.py
## USAGE: From shell prompt: python3 duration.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Experiment to measure duration 
##              of random walk of n steps done k times each,
##              starting from each value from ruin to victory,
##              continuing until reaching either ruin or victory
##              equivalent to absorbing random walk, or gambler's ruin
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES: requires matplotlib
## INCOMPATIBILITIES: none known
## PROVENANCE:  Steven R. Dunbar Wed Aug  8, 2012  5:30 AM
## BUGS AND LIMITATIONS: None known
## FEATURES AND POTENTIAL IMPROVEMENTS:  
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Wed Aug  8, 2012  5:33 AM
##          Version 1.1 as of Tue Mar  1, 2016  7:31 AM, upgrade to python3
##          Version 1.2 as of Fri Mar 11, 2016  7:40 AM  add matplotlib graphics
## KEYWORDS: Coin flips, Gambler's Ruin, Absorbing Random Walk


