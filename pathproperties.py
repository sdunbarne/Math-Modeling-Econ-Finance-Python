#! /usr/bin/env python3

import scipy
import matplotlib.pyplot as plt

p = 0.5

N = 1000
T = 1.

# the random walk
S = scipy.zeros(N+1)
S[1:N+1] = scipy.cumsum( 2*( scipy.random.random(N) <= p ) - 1 )

def WcaretN(x):
    Delta = T/N
    prior = scipy.floor(x/Delta).astype(int)
    subsequent = scipy.ceil(x/Delta).astype(int)
    return scipy.sqrt(Delta)*(S[prior] + (x/Delta - prior)*(S[subsequent] - S[prior]))

h0 = 1e-7
h1 = 1e-2
m = 30
basepoint = 0.5

h = scipy.linspace( h0, h1, m)
x0 = basepoint * scipy.ones(30)

diffquotients = scipy.absolute( WcaretN( x0 + h ) - WcaretN( x0 ) )/h

plt.plot(h,diffquotients)
plt.xlabel('h')
plt.ylabel('|W(x0+h)-W(x0)|/h')
plt.show()


# optional file output to use with external plotting programming
# such as gnuplot, R, octave, etc. 
# Start gnuplot, then from gnuplot prompt
#    set logscale y
#    plot "pathproperties.dat" with lines
# f = open('pathproperties.dat', 'w')
# for j in range(0, m-1):
#     f.write( str(h[j])+' '+str(diffquotients[j])+'\n');
# f.close()

## NAME: pathproperties.py
## USAGE: From shell prompt: python3 pathproperties.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: 
##   Using a scaled random walk approximation of the Wiener process,
##   find the difference quotients on an array of differences based at
##   single point, then plot the absolute values of the difference quotients
##   to illustrate the non-existence of the derivative.
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES: requires matplotlib
## INCOMPATIBILITIES: None known
## PROVENANCE: Created by sdunbar, very loosely based on example 
##             ex1.07.R on page 20-21 in \emph{Simulation
##	       and Inference for Stochastic Differential
##	       Equations}, by Stefano Iacus, Springer, 2008
## BUGS AND LIMITATIONS: none known
## FEATURES AND POTENTIAL IMPROVEMENTS:
##   The difference quotients take advantage of the design of
##   WcaretN as vector-capable, that is, the input can be
##   a vector or array, and the output will be a vector of values of the 
##   approximation function at the corresponding points.
##   Because the difference quotients are computed using the scaled random
##   walk approximation of the Wiener process, the largest possible slope is
##   sqrt(T/N)/(T/N) = sqrt(N/T).  So the plotted difference quotients will 
##   max out once the increment is less than the scaled random walk step size.
##   Should add some plotting from within python
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Wed Jul 10, 2013  6:11 AM
## KEYWORDS: random walk, Wiener process, Brownian motion, path properties,
##           derivative

