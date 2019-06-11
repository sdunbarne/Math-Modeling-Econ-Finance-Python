#! /usr/bin/env python3

import scipy

T = 10.0
# note type float
a = 1
time = 2

p = 0.5
n = 1000
k = 50

Delta = T/n

winLose = 2*( scipy.random.random((n,k)) <= p ) - 1
totals = scipy.cumsum(winLose, axis = 0)

paths = scipy.zeros((n+1,k), dtype=float)
paths[ 1:n+1, :] = scipy.sqrt(Delta) * totals

def match(x,arry,nomatch=None):
    if arry[scipy.where( (arry >= x))].any(): 
        return  scipy.where( (arry >= x) )[0][0] - 1
    else:
        return nomatch
# arguments: x is a scalar, arry is a python list, value of nomatch is scalar
# returns the first index of first  of its first argument in its second argument
# but if a is not there, returns the value nomatch
# modeled on the R function "match", but with less generality

hitIndex = scipy.apply_along_axis(lambda x:( match(a,x,nomatch=n+2)), 0, paths)
# If no ruin or victory on a walk, nomatch=n+2 sets the hitting
# time to be two more than the number of steps, one more than
# the column length.

hittingTime = Delta * hitIndex

probHitlessTa = (scipy.sum( hittingTime < time).astype('float'))/k
probMax = (scipy.sum( scipy.amax( paths[ 0:scipy.floor(time/Delta)+1, : ], axis=0) >= a).astype('float'))/k
from scipy.stats import norm
theoreticalProb = 2 * (1 - norm.cdf(a/scipy.sqrt(time)))

print "Empirical probability Wiener process paths hit ", a, "before ", time, "is ", probHitlessTa
print "Empirical probability Wiener process paths greater than ", a, "before ", time, "is ", probMax
print "Theoretical probability:", theoreticalProb

## NAME: hittingtime.pl
## USAGE: From shell prompt: python3 hittingtime.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Experiment of approximating Wiener process over [0,T]
##              k times, finding the time of hitting a, then computing
##              the fraction out of k with hitting time less or equal to
##              t.  Also compute the maximum over [0,t], compute
##              fraction out of k with maximum greater or equal to a.
## DIAGNOSTICS: None
## CONFIGURATION AND ENVIRONMENT: None
## DEPENDENCIES: None
## INCOMPATIBILITIES: None known
## PROVENANCE: Created Mon Jun 17, 2013  5:26 AM
## BUGS AND LIMITATIONS:  none
## FEATURES AND POTENTIAL IMPROVEMENTS:
## Need better formating for the output.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 Mon Jun 17, 2013  5:27 AM
## KEYWORDS: Wiener process, Brownian Motion, hitting time,
##           distribtion of maximum
