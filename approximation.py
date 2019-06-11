#! /usr/bin/env python3

import scipy
import matplotlib.pyplot as plt

p = 0.5

N = 400
T = 1.

# the random walk
S = scipy.zeros(N+1)
S[1:N+1] = scipy.cumsum( 2*( scipy.random.random(N) <= p ) - 1 )

def WcaretN(x):
    Delta = T/N
    prior = scipy.floor(x/Delta).astype(int)
    subsequent = scipy.ceil(x/Delta).astype(int)
    return scipy.sqrt(Delta)*(S[prior] + (x/Delta - prior)*(S[subsequent] - S[prior]))

M = 300
tgrid = scipy.linspace(0, T, M+1)
W = WcaretN(tgrid)

plt.plot(tgrid,W)
plt.show()

# optional file output to use with external plotting programming
# such as gnuplot, R, octave, etc. 
# Start gnuplot, then from gnuplot prompt
#    plot "wienerprocess.dat" with lines
# f = open('wienerprocess.dat', 'w')
# for j in range(0,M+1):
#     f.write( str(tgrid[j])+' '+str(W[j])+'\n');

# f.close()

## NAME: approximation.py
## USAGE: From shell prompt: python3 approximation.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Approximation of Wiener process using the
##              scaling approximation of random walk
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES: requires matplotlib
## INCOMPATIBILITIES: none known
## PROVENANCE: Created by Steve Dunbar
## BUGS AND LIMITATIONS: No bugs known.
## FEATURES AND POTENTIAL IMPROVEMENTS:  
##  The function assumes the inputs are in the interval [0,T]
##  Better input checking could catch errors before plotting.
##   The function WcaretN is vector-capable, that is, the input can be
##   a vector or array, and the output will be a vector of values of the
##   approximation function at the corresponding points.
##  A feature of this \( N + 1 \)-step random walk scaling approximation
##  algorithm is that it creates the approximation as a function on \( [0,T]
##  \).  This function can then be plotted with a function plotting
##  routine on any time grid on the interval
##  \( [0,T] \).  If the time grid used for plotting on \( [0,T] \) is
##  less than \( N \) points, then some of the information in the \( N
##  \)-step scaling approximation is ignored, and the plotted function
##  will be less representative of the approximation than it could be.  If
##  the time grid on \( [0,T] \) is greater than \( N \) points, then the
##  plotted function will just represent the linear interpolation between
##  the random-walk points at \(t_j = jT/N \) and no new information is
##  represented.
##  Depending on the internal plotting routines used by the language,
##  plotting the approximation function \( \hat{W}_N(t) \) can result in
##  plot artifacts.  One simple artifact may be horizonal segments in the
##  points. If the plotting algorithms attempt to use adaptive point
##  selection to densely position a greater portion of a fixed number of
##  plotting points in a region of rapid variation, then other regions
##  will have fewer plotting points.  Those regions with fewer plotting
##  points will miss some of the information in that region.  Depending on
##  the language, the plotting routine may use smoothing or some other
##  nonlinear interpolation between plotting points which will result in
##  curved segments instead of a piecewise linear function.  If the
##  intention is to plot an approximate Brownian Motion, then there are
##  more direct and efficient ways to create and plot the \( N+1 \)
##  coordinate pairs \( (jT/N, \sqrt{T/N} S_{j}) \) defining the vertices of the
##  piecewise linear scaled random walk approximation with an appropriate amount of
##  information.  Here the intention is to first to demonstrate the
##  creation of the approximation function as a piecewise linear function,
##  then second to use the function to plot a graph.

## AUTHOR:  Steve Dunbar
## VERSION: 1.0 as of Wed May  1, 2013  5:49 AM
##          1.1. as of Fri Mar 11, 2016  7:38 AM
## KEYWORDS: random walk, Wiener process, Brownian motion


