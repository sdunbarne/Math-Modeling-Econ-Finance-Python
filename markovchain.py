#! /usr/bin/env python3

import scipy

n = 10;   # Top boundary, number of states 0..n is n+1
s = 5;   # Start and Reset state number 1 <= s <= n-1
p = 0.5;
steps = 1000;

T = scipy.diag( p*scipy.ones( n ), 1) + scipy.diag( (1-p)*scipy.ones( n ), -1);
T[0,1] = 0; T[0,s] = 1;
T[n,n-1] = 0; T[n,s] = 1;

# vector to hold the count of visits to each state during a cycle
count = scipy.zeros(n+1, float);
# Initialize the cyclelength
numberCycles = 0;
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
        avgVisits = count/numberCycles;
        avgCycleLength = i/numberCycles;

Wsk = avgVisits
theoreticalWsk = 2*(  s*(1-scipy.arange(0,n+1,dtype=float)/n) - scipy.maximum(s-scipy.arange(0,n+1), scipy.zeros(n+1, int) ) ) 
print( "Average number of visits to each state in a cycle:\n ", Wsk)
print( "Theoretical number of visits to each state in a cycle: \n", theoreticalWsk)

## NAME:  markovchain.py
## USAGE:  From shell prompt: python3 markovchain.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Simulation of the cash management model as a Markov chain
## DIAGNOSTICS: None
## CONFIGURATION AND ENVIRONMENT: None
## DEPENDENCIES: None
## INCOMPATIBILITIES: None known
## PROVENANCE: Tue Aug 28, 2012  5:38 AM
## BUGS AND LIMITATIONS:  None Known
## FEATURES AND POTENTIAL IMPROVEMENTS:
## For the innermost for-loop, you can simply use 
## newState = scipy.random.choice(1, 1, prob=T[state,])
## That shows more clearly what's going on 
## On the other hand, if other languages don't have a function comparable to sample, then
## the current formulation is easier to adapt and make the algorithms similar.

## AUTHOR:  Steve Dunbar
## VERSION: 1.0 Tue Aug 28, 2012  5:38 AM
##          1.1 added some ouput formatting Mon Nov 12, 2012  6:03 AM
## KEYWORDS:   Markov chain, simulation, reflecting boundary

