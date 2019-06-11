#! /usr/bin/env python3

import scipy

p = 0.5
n = 100
k = 30

coinFlips = scipy.random.random((n,k))<= p  
# Note Booleans True for Heads and False for Tails
totals = scipy.cumsum(2*coinFlips-1, axis = 0)
# Note how Booleans act as 0 (False) and 1 (True)

victory = 10;                   # top boundary for random walk
ruin = -10;                     # bottom boundary of random walk

victoryOrRuin = scipy.zeros(k,int);
hitVictory = scipy.argmax( (totals >= victory), axis=0)
hitRuin = scipy.argmax( (totals <= ruin), axis=0)
for i in range(k): 
    if hitVictory[i] == 0 and  hitRuin[i] == 0:
        # no victory, no ruin, do nothing
        victoryOrRuin[i] = 0
    elif hitVictory[i] > 0 and  hitRuin[i] == 0:
        victoryOrRuin[i] = hitVictory[i] 
    elif hitVictory[i] == 0 and  hitRuin[i] > 0:
        victoryOrRuin[i] = -hitRuin[i]
    else:
        if hitVictory[i] < hitRuin[i]:
            victoryOrRuin[i] = hitVictory[i]
        else:
            victoryOrRuin[i] = -hitRuin[i]

victoryBeforeRuin = sum( victoryOrRuin > 0 ) # count exits through top
ruinBeforeVictory = sum( victoryOrRuin < 0 ) # count exits through bottom
noRuinOrVictory   = sum( victoryOrRuin == 0 )

print( "Victories:", victoryBeforeRuin, "Ruins:", ruinBeforeVictory)
print( "No Ruin or Victory:",  noRuinOrVictory)

avgTimeVictoryOrRuin = scipy.mean( abs(victoryOrRuin) )
stdTimeVictoryOrRuin = scipy.std( abs(victoryOrRuin) )
varTimeVictoryOrRuin = stdTimeVictoryOrRuin * stdTimeVictoryOrRuin

print( "Average Time to Victory or Ruin:", avgTimeVictoryOrRuin)
print( "Variance of Time to Victory or Ruin:",  varTimeVictoryOrRuin)

## NAME:  victoryorruin.py
## USAGE: within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: must run experiment.py first to have array totals
## OPTIONS: none
## DESCRIPTION: After experiment, find, count and display the hitting
##              times for victory (exit through top boundary) or ruin 
##             (exit through bottom boundary) 
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT:  environment is python interpreter, configuration is none
## DEPENDENCIES:  experiment.py
## INCOMPATIBILITIES: none known
## PROVENANCE: Created Tue Mar  6, 2012  6:02 AM
## BUGS AND LIMITATIONS: None known
## FEATURES AND POTENTIAL IMPROVEMENTS: Should produce a graph, a visualization

## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Tue Mar  6, 2012  6:03 AM
##                  1.1 print formatting Thu Nov  1, 2012  6:02 AM
##          Version 1.2 as of Tue Mar  1, 2016  7:31 AM, upgrade to python3
## KEYWORDS: Hitting times, coin flips, random walk
## AUTHOR:  Steve Dunbar


