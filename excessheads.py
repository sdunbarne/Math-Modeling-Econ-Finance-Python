#! /usr/bin/env python3
 
import scipy

p = 0.5
n = 500
k = 1000

coinFlips = scipy.random.random((n,k))<= p  
# Note Booleans True for Heads and False for Tails
winLose = 2*coinFlips - 1
excessHeads = scipy.sum(winLose, axis = 0)

s = 20
prob = (scipy.sum( abs(excessHeads) > s )).astype('float')/k
# Note the casting of integer type to float to get float
from scipy.stats import norm
theoretical = 2*(1-norm.cdf( (s+0.5)/scipy.sqrt(n)))

print( "Empirical probability: ", prob)
print( "Excess heads theoretical estimate:", theoretical)

## NAME:  excessheads.py
## USAGE:  From shell prompt: python3 excessheads.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS:  none
## OPTIONS:  none
## DESCRIPTION:  Experiment of flipping a coin n times
##               and repeat the experiment k times
##               Compare probability of excess binomial
##               to standard normal cdf
## DIAGNOSTICS:  none
## CONFIGURATION AND ENVIRONMENT:  none
## DEPENDENCIES:  none
## INCOMPATIBILITIES:  none known
## PROVENANCE:  Created Mon Dec 24, 2012  7:09 AM
## BUGS AND LIMITATIONS:  None known
## FEATURES AND POTENTIAL IMPROVEMENTS:  None at this time

## AUTHOR:  Steve Dunbar
## VERSION:  Version 1.0 as of Mon Dec 24, 2012  7:09 AM
## KEYWORDS: Coin flips, binomial random variable
##           DeMoivre-Laplace Central Limit Theorem


