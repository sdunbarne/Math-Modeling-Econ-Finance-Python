#! /usr/bin/env python3

import scipy

p = 0.5

N = 400
T = 2.
h = 0.25
c = 2.0

# the random walk
S = scipy.zeros(N+1)
S[1:N+1] = scipy.cumsum( 2*( scipy.random.random(N) <= p ) - 1 )

def WcaretN(x):
    Delta = T/N
    prior = scipy.floor(x/Delta).astype(int)
    subsequent = scipy.ceil(x/Delta).astype(int)
    return scipy.sqrt(Delta)*(S[prior] + (x/Delta - prior)*(S[subsequent] - S[prior]))

def Wshift(x):
    return WcaretN(x + h) - WcaretN(h)

def Wscale(x):
    return c*WcaretN(x/c**2.)

M = 300
tgrid = scipy.linspace(0, 1, M+1)
W = WcaretN(tgrid)
Wsh = Wshift(tgrid)
Wsc = Wscale(tgrid)

# optional file output to use with external plotting programming
# such as gnuplot, R, octave, etc. 
# Start gnuplot, then from gnuplot prompt
#  plot "wienerprocess.dat" using 1:2 with lines title 'WcaretN', "wienerprocess.dat" using 1:3 with lines title 'Wshift', "wienerprocess.dat" using 1:4 with lines title 'Wscale'
f = open('wienerprocess.dat', 'w')
for j in range(0,M+1):
    f.write( str(tgrid[j])+' '+str(W[j])+' '+str(Wsh[j])+' '+str(Wsc[j])+'\n');

f.close()

## NAME: transformations.py
## USAGE: From shell prompt: python3 transformations.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Transformations of Wiener process using the
##              scaling approximation of random walk
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: none
## DEPENDENCIES: none
## INCOMPATIBILITIES: none known
## PROVENANCE: Created by Steve Dunbar
## BUGS AND LIMITATIONS: No bugs known, but because I have chosen to
##      NOT use the optional and extra PDL graphics packages, the
##      limitation is no plotting or graphical display.
##      To get some graphics, export to an outside utility, including
##      gnuplot.
## FEATURES AND POTENTIAL IMPROVEMENTS:  An improvement is to add in a
##   graphics package.
##  The base approximation function assumes the inputs are in the interval [0,T]
##  The transformed functions assume the inputs are compatible with the base
##  approximation function.
##  Better input checking could catch errors before plotting.
##   The function WcaretN is vector-capable, that is, the input can be
##   a vector or array, and the output will be a vector of values of the
##   approximation function at the corresponding points.
##   The transformed functions are correspondingly vactor-capable.
##   A feature of this N-step random walk scaling approximation program
##   is that it creates the approximation and the transformations as functions
##   on [0,T].  All
##   functions can be plotted with any number of points on the interval [0,T].
##   If the time grid on [0,T] is less than N points, then some of the
##   information in the N-step scaling approximation is ignored, and the
##   plotted function will be less representative of the approximation
##   than it could be.  If the time grid on [0,T] is is greater than N
##   points, then the plotted function will just represent the linear
##   interpolation between the step points at j*T/N and no new
##   information is represented.
##  Depending on the internal plotting routines used by the language,
##  plotting the approximation and transformed functions
##  can result in
##  plot artifacts.  One simple artifact may be horizonal segments in the
##  points. If the plotting algorithms attempt to use adaptive point
##  selection to densely position a greater portion of a fixed number of
##  plotting points in a region of rapid variation, then other regions
##  will have fewer plotting points.  Those regions with fewer plotting
##  points will miss some of the information in that region.  Depending on
##  the language, the plotting routine may use smoothing or some other
##  nonlinear interpolation between plotting points which will result in
##  curved segments instead of a piecewise linear function.  If the
##  intention is to plot an transformed Brownian Motion, then there are
##  more direct and efficient ways to create and plot the \( N+1 \)
##  coordinate pairs \( (jT/N, \sqrt{T/N} S_{j}) \) defining the vertices of the
##  piecewise linear scaled random walk approximation with an appropriate amount of
##  information.  Here the intention is to first to demonstrate the
##  creation of the approximation function as a piecewise linear function,
##  then second to use the function to plot a graph.
## AUTHOR:  Steve Dunbar
## VERSION: 1.0 as of Fri May 17, 2013  5:34 AM
## KEYWORDS: random walk, Wiener process, Brownian motion, transformation


