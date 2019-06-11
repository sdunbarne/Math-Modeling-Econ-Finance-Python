#! /usr/bin/env python3

import scipy

p = 0.5
n = 100
k = 30

coinFlips = scipy.random.random((n,k))<= p  
# Note Booleans True for Heads and False for Tails
headsTotal = scipy.sum(coinFlips, axis = 0)
# Note how Booleans act as 0 (False) and 1 (True)
muHeads = scipy.mean(headsTotal)
stddevHeads = scipy.std(headsTotal)
sigmaSquaredHeads = stddevHeads * stddevHeads
print( "Empirical Mean of Heads:", muHeads)
print( "Empirical Variance of Heads:", sigmaSquaredHeads)

winLose = 2*coinFlips - 1
totals = scipy.cumsum(winLose, axis = 0)
muWinLose = scipy.mean(totals[n-1,range(k)])
stddevWinLose = scipy.std(totals[n-1, range(k)])
sigmaSquaredWinLose = stddevWinLose * stddevWinLose
print( "Empirical Mean of Wins minus Losses:", muWinLose)
print( "Empirical Variance of Wins minus Losses:",  sigmaSquaredWinLose)

## NAME:  experiment.py
## USAGE:  From shell prompt: python3 experiment.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS:  none
## OPTIONS:  none
## DESCRIPTION:  Experiment of flipping a coin n times
##               and repeat the experiment k times
## DIAGNOSTICS:  none
## CONFIGURATION AND ENVIRONMENT:  none
## DEPENDENCIES:  none
## INCOMPATIBILITIES:  none known
## PROVENANCE:  Created Tue Mar  6, 2012  5:40 AM
## BUGS AND LIMITATIONS:  None known
## FEATURES AND POTENTIAL IMPROVEMENTS:  None at this time
## AUTHOR:  Steve Dunbar
## VERSION:  Version 1.0 as of Tue Mar  6, 2012  5:40 AM
##                   1.1 fixed typos, added print formatting Thu Nov  1, 2012  5:55 AM
##           Version 1.2 as of Tue Mar  1, 2016  7:31 AM, upgrade to python3
## KEYWORDS: Coin flips, binomial random variable

