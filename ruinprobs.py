#! /usr/bin/env python3

import scipy
import matplotlib.pyplot as plt

p = 0.5
n = 150
k = 60
victory = 10;
ruin = -10;
interval = victory - ruin + 1;

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

probRuinBeforeVictory = scipy.mean( (hitRuin < hitVictory), axis=0)
# note that you can treat the bool's as binary data!

startValues = scipy.arange(ruin, victory+1, dtype=int)
ruinFunction = scipy.polyfit( startValues, probRuinBeforeVictory, 1)
print( "Ruin function Intercept:", ruinFunction[1])
print( "Ruin function Slope:", ruinFunction[0])
# should return a slope near -1/(victory-ruin) and an intercept near 0.5

plt.scatter(startValues, probRuinBeforeVictory)
X = scipy.linspace(ruin, victory, 256, endpoint=True)
Y = ruinFunction[1] + ruinFunction[0]*X
plt.plot(X,Y)
plt.show()

## NAME: ruinprobs.py
## USAGE: From shell prompt: python3 ruinprobs.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Experiment of random walk of n steps done k times each,
##              starting from each value from ruin to victory,
##              continuing until reaching either ruin or victory
##              equivalent to absorbing random walk, or gambler's ruin
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES: requires matplotlib
## INCOMPATIBILITIES: none known
## PROVENANCE:  Tue Jul  3, 2012  5:51 AM
## BUGS AND LIMITATIONS: None known
## FEATURES AND POTENTIAL IMPROVEMENTS:  
##   Creating this script was more difficult for me than it should have
##   been.  One cause of problems is the variety of data types in scipy.
##   A further problem was the more or less silent coercing of one type
##   into another type, which latter type is incompatible with some
##   function.  For example, while creating the "start" ndarray with the
##   outer function one way to do it is:
   
##   start = scipy.multiply.outer( scipy.ones((n+1,k), int), scipy.linspace(ruin, victory, num=interval))

##   However, in creating "start", "scipy.ones((n+1,k), int)" has type
##   integer, more precisely, dtype reveals it is of type int64.  On the
##   other hand, "scipy.linspace(ruin, victory, num=interval).dtype"
##   reveals that "scipy.linspace(ruin, victory, num=interval)" is of
##   dtype float64 Hence "start.dtype" reveals that "start" is of type
##   float64.  Then it later turns out some logic and masking functions
##   do not work well with floats.  The solution is to use the less
##   obvious "scipy.arange(ruin, victory+1, dtype=int)" to create the
##   integral array which spans from "ruin" to "victory".
##   Once I had the ndarray "paths", I wanted to find which random walks
##   had "ruin" first, which "paths" had victory first, and which random
##   walks hit neither "ruin" nor "victory".  A seemingly natural
##   approach, especially in comparison with R and PDL, uses masked
##   arrays with the mask value or the fill_value to mark those paths
##   which had not yet hit "ruin" or "victory".  Then using the functions
##   "scipy.argmin" and "scipy.argmax" seem to be the right way to find
##   where ruin and victory occur.  Unfortunately, if the "hitVictory"
##   column which is argmin-ed is all masked, the output is 0 which is
##   the same as if the min occurs at position 0. This confuses two
##   outcome possibilities with the same value!  As another alternative, I
##   tried using logical values derived from the masks.  There are many
##   masked_array functions, maybe too many, since I tried many
##   variations to create logical arrays marking ruin or victory.
##   However, the logic got quite convoluted.  There are four possible
##   combinations: neither ruin nor victory; ruin but never victory;
##   victory but never ruin; and ruin before victory.  I could combine
##   logical arrays to get three of the four, but I could not easily make
##   all four logical combinations.  This was clearly a dead-end,
##   creating program logic which was going to be hard to understand and
##   maintain.
##   Finally, I decided it would be easier to write my own new scipy 
##   function match which acted the same as the match function which
##   I found in R.  A Google search 
##   found a StackOverflow question and answer for precisely
##   this situation.  The solution is
##   >>> a = [5,4,3,2,1]
##   >>> b = [2,3]
##   >>> [ b.index(x) if x in b else None for x in a ]
##   [None, None, 1, 0, None]
##   However, this function works for python arrays, but scipy ndarrays do not
##   have columns which are arrays. Instead it appears that accessing a column
##   of a scipy ndarray yields an integer pointer.  Therefore, simply
##   copying this definition does not immediately work.  Hence I had to
##   simplify the function definition, making it less
##   general by only allowing argument "a" to be a scalar but more general by
##   creating the nomatch option when failing to find the match.
##  Finally, using the very natural function scipy.apply_along_axis is
##  is great, but seems to be slow according to some comments in
##  stackoverflow.org Finally, I have to do a lot of type conversions to
##  get this correctly on scipy ndarrays.
##  There may be a simpler cleaner approach for the whole with fewer type conversions, 
##  but this seems to work for now.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Tue Jul  3, 2012  5:51 AM
##          Version 1.1 as of Tue Mar  1, 2016  7:31 AM, upgrade to python3
##          Version 1.2 as of Thu Mar 10, 2016  5:51 AM, added plotting
## KEYWORDS: Coin flips, Gambler's Ruin, Absorbing Random Walk


