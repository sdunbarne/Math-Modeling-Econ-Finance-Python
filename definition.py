#! /usr/bin/env python3

import scipy
import matplotlib.pyplot as plt

N = 100
T = 1.
Delta = T/N

# initialization of the vector W approximating
# Wiener process
W = scipy.zeros(N+1)

t = scipy.linspace(0, T, N+1);
W[1:N+1] = scipy.cumsum(scipy.sqrt(Delta)*scipy.random.standard_normal(N))

print( "Simulation of the Wiener process:\n", W)
 
plt.plot(t,W)
plt.xlabel('t')
plt.ylabel('W')
plt.title('Wiener process')
plt.show()

## optional file output to use with external plotting programming
## such as gnuplot, R, octave, etc. 
## Start gnuplot, then from gnuplot prompt
##    plot "wienerprocess.dat" with lines
# f = open('wienerprocess.dat', 'w')
# for j in range(0,N+1):
#     f.write( str(t[j])+' '+str(W[j])+'\n');

# f.close()

## NAME: definition.py
## USAGE: From shell prompt: python3 definition.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## DESCRIPTION: Simulation of Wiener process using the
##              definition as independent increments having
##		normal distribution with variance sqrt(Delta)
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES:  requires matplotlib
## INCOMPATIBILITIES: none known
## PROVENANCE: Created by sdunbar, based on example
## BUGS AND LIMITATIONS: no bugs known.
## FEATURES AND POTENTIAL IMPROVEMENTS:  An improvement is to add in a
##   graphics package.
## AUTHOR:  Steve Dunbar
## VERSION: 1.0, as of Wed Mar  6, 2013  6:08 AM
##          1.1. as of Fri Mar 11, 2016  7:36 AM
## KEYWORDS: Wiener process, Brownian motion

