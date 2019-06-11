#! /usr/bin/env python3

import scipy

n = 10;   # Top boundary, number of states 0..n is n+1
s = 5;   # Start and Reset state number 1 <= s <= n-1
p = 0.5;
steps = 1000;
rate = 1.0
K = 2.0

T = scipy.diag( p*scipy.ones( n ), 1) + scipy.diag( (1-p)*scipy.ones( n ), -1);
# square brakets okay, assignment not
T[0,1] = 0; T[0,s] = 1;
T[n,n-1] = 0; T[n,s] = 1;

# vector to hold the count of visits to each state during a cycle
count = scipy.zeros(n+1, float);
# Initialize the cyclelength
numberCycles = 0;
# Initialize the total cost of the cashmanagement
totalCost = 0.0
# Start in the state s
state = s;

# Make steps through the markov chain
for i in range(1, steps+1):
    x = 0;
    u = scipy.random.random(1);
    newState = state;
    for j in range(n+1):
        x = x + T[state, j];
        if (x >= u):
            newState = j;
            break;
    ## newState = scipy.random.choice(1, 1, prob=T[state,])
    state = newState;
    count[state] = count[state] + 1;
    
    if (state == n or state == 0):
        numberCycles = numberCycles + 1;
        totalCost = K + totalCost
    else:
        totalCost = rate*state + totalCost

avgCost = totalCost/steps
theoreticalAvgCost = ( K + (1./3.)*(rate*s*(n**2 - s**2)) )/( s*(n-s) )
print( "Average cost:\n ", avgCost)
print( "Theoretical average cost: \n", theoreticalAvgCost)


## NAME:  cashmanagement.py
## USAGE:  From shell prompt: python3 cashmanagement.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Simulation of the cash management model as a Markov chain
## DIAGNOSTICS: None
## CONFIGURATION AND ENVIRONMENT: None
## DEPENDENCIES: None
## INCOMPATIBILITIES: None known
## PROVENANCE: Tue Aug 28, 2012  6:05 AM
## BUGS AND LIMITATIONS:  None Known
## FEATURES AND POTENTIAL IMPROVEMENTS:
## For the innermost for-loop, you can simply use 
## newState = scipy.random.choice(1, 1, prob=T[state,])
## That shows more clearly what's going on 
## On the other hand, if other languages don't have a function comparable to sample, then
## the current formulation is easier to adapt and make the algorithms similar.

## AUTHOR:  Steve Dunbar
## VERSION: 1.0 Tue Aug 28, 2012  6:05 AM
##          1.1 Tue Nov 13, 2012  5:42 AM, added output formatting
## KEYWORDS:   Markov chain, simulation, reflecting boundary

