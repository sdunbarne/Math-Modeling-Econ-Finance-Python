#! /usr/bin/env python3
 
import scipy

p = 0.5
n = 10000
k = 1000

coinFlips = scipy.random.random((n,k))<= p  
# Note Booleans True for Heads and False for Tails
headsTotal = scipy.sum(coinFlips, axis = 0)
# 0..n binomial r.v. sample, size k
# Note how Booleans act as 0 (False) and 1 (True)

epsilon = 0.01
mu = p

prob = (scipy.sum( abs( headsTotal.astype('float')/n - mu)  >  epsilon)).astype('float')/k
# Note the casting of integer types to float to get floats

print( "Empirical probability: ", prob)

## NAME:  lawlargenumbers.py
## USAGE:  From shell prompt: python3 lawlargenumbers.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS:  none
## OPTIONS:  none
## DESCRIPTION:  Experiment of flipping a coin n times
##               and repeat the experiment k times
## DIAGNOSTICS:  none
## CONFIGURATION AND ENVIRONMENT:  none
## DEPENDENCIES:  none
## INCOMPATIBILITIES:  none known
## PROVENANCE:  Created Tue Dec  4, 2012  7:07 AM
## BUGS AND LIMITATIONS:  None known
## FEATURES AND POTENTIAL IMPROVEMENTS:  None at this time

## AUTHOR:  Steve Dunbar
## VERSION:  Version 1.0 as of Tue Dec  4, 2012  7:08 AM
## KEYWORDS: Coin flips, binomial random variable

