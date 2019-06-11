#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scipy
import matplotlib.pyplot as plt

mu = 0.1682262
sigma = 0.1722922
T = 5.75

# length of the interval [0, T] in time units

S0 = 8242.38

N = 1448

# number of end-points of the grid including T

Delta = T / N

# time increment

W = scipy.zeros(N + 1, dtype=float)

# initialization of the vector W approximating
# Wiener process

t = scipy.ones(N + 1, dtype=float) * scipy.linspace(0, T, N + 1)

# Note the use of recycling

W[1:N + 1] = scipy.cumsum(scipy.sqrt(Delta)
                          * scipy.random.standard_normal(N))

GBM = S0 * scipy.exp(mu * t + sigma * W)

plt.plot(t,GBM)
plt.xticks([ 0.75, 1.75, 2.75, 3.75, 4.75, 5.75],
           ["2010", "2011", "2012", "2013", "2014", "2015"])
plt.xlabel('t')
plt.ylabel('Simulated Wilshire 5000 Index')
plt.show()



# optional file output to use with external plotting programming
# such as gnuplot, R, octave, etc.
# Start gnuplot, then from gnuplot prompt
#    plot "stockmarketmodel.dat" with lines;\
#    set xtic ("2010" 0.75, "2011" 1.75, "2012" 2.75, "2013" 3.75, "2014" 4.75, "2015" 5.75)

# f = open('stockmarketmodel.dat', 'w')
# for j in range(0, N):
#     f.write(str(t[j]) + ' ' + str(GBM[j]) + '\n')
# f.close()

## NAME: stockmarketmodel.py
## USAGE: from shell prompt: python3 stockmarketmodel.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Create a Geometric Brownian Motion with the same
## parameters as the Wilshire 5000 Index over the period April 1, 2009 to
## December 31, 2014
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES: requires matplotlib
## INCOMPATIBILITIES: none known
## PROVENANCE: created by sdunbar
## BUGS AND LIMITATIONS: No bugs known, but because I have chosen to
##      NOT use the optional and extra scipy graphics packages, the
##      limitation is no plotting or graphical display.
##      To get some graphics, export to an outside utility, including
##      R, octave, or gnuplot.
## FEATURES AND POTENTIAL IMPROVEMENTS:
##   1. Would be good to include the actual Wilshire 5000 data over the period
##   April 1, 2009, to December 31, 2015, but that would require a way to
##   incorporate the 1449 dates and corresponding data values.
##   2.  Profiling shows no obvious bottlenecks or hotspots
## AUTHOR:  Steve Dunbar
## VERSION: 1.0 as of Thu Sep 10, 2015  5:41 AM
##          1.1. as of Fri Mar 11, 2016  7:47 AM, added graphics
## KEYWORDS: Wiener process, Brownian Motion, Geometric Brownian
## Motion, relative growth rate, Wilshire 5000

