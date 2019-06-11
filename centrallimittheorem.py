#! /usr/bin/env python3
 
import scipy

p = 0.5
n = 10000
k = 1000

coinFlips = scipy.random.random((n,k))<= p  
# Note Booleans True for Heads and False for Tails
headsTotal = scipy.sum(coinFlips, axis = 0) # 0..n binomial r.v. sample, size k
# Note how Booleans act as 0 (False) and 1 (True)

mu = p
sigma = scipy.sqrt( p * ( 1-p ) )
a = 0.5
Zn = (headsTotal - n*mu)/(sigma * scipy.sqrt(n))

prob = (scipy.sum( Zn < a )).astype('float')/k
# Note the casting of integer type to float to get float
from scipy.stats import norm
theoretical = norm.cdf(a)

print( "Empirical probability: ", prob)
print( "Central Limit Theorem estimate:", theoretical)

## NAME:  centrallimittheorem.py
## USAGE:  From shell prompt: python3 centrallimittheorem.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS:  none
## OPTIONS:  none
## DESCRIPTION:  Experiment of flipping a coin n times
##               and repeat the experiment k times
##               Compare probability of normalized binomial
##               to standard normal cdf
## DIAGNOSTICS:  none
## CONFIGURATION AND ENVIRONMENT:  none
## DEPENDENCIES:  none
## INCOMPATIBILITIES:  none known
## PROVENANCE:  Created Tue Dec 18, 2012  5:33 AM
## BUGS AND LIMITATIONS:  None known
## FEATURES AND POTENTIAL IMPROVEMENTS:  None at this time

## AUTHOR:  Steve Dunbar
## VERSION:  Version 1.0 as of Tue Dec 18, 2012  5:34 AM
##           Version 1.1, fixed output labeling, Fri Mar 18, 2016  5:22 AM
## KEYWORDS: Coin flips, binomial random variable
##           DeMoivre-Laplace Central Limit Theorem


