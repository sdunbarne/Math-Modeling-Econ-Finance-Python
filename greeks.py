#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scipy
import matplotlib.pyplot as plt

m = 6
n = 61
S0 = 70
S1 = 130
K = 100
r = 0.12
T = 1.0
sigma = 0.10

time = scipy.linspace(T, 0.0, m)
S = scipy.linspace(S0, S1, n)

logSoverK = scipy.log(S / K)
n12 = (r + sigma ** 2 / 2) * (T - time)
numerd1 = logSoverK[scipy.newaxis, :] + n12[:, scipy.newaxis]
d1 = numerd1 / (sigma * scipy.sqrt(T - time)[:, scipy.newaxis])

from scipy.stats import norm
Delta = norm.cdf(d1)

denom1 = (scipy.sqrt(2 * scipy.pi) * sigma * scipy.sqrt(T - time))[:,
        scipy.newaxis]
factor1 = 1 / (denom1 * S)
factor2 = scipy.exp(-d1 ** 2 / 2)
Gamma = factor1 * factor2

plt.subplot(121)
plt.plot(S, Delta[0,:])
plt.plot(S, Delta[1,:])
plt.plot(S, Delta[2,:])
plt.plot(S, Delta[3,:])
plt.plot(S, Delta[4,:])
plt.plot(S, Delta[5,:])
plt.xlabel('S')
plt.ylabel('Delta')

plt.subplot(122)
plt.plot(S, Gamma[0,:])
plt.plot(S, Gamma[1,:])
plt.plot(S, Gamma[2,:])
plt.plot(S, Gamma[3,:])
plt.plot(S, Gamma[4,:])
plt.plot(S, Gamma[5,:])
plt.xlabel('S')
plt.ylabel('Gamma')

plt.show()

# file output to use with external plotting programming
# such as gnuplot, R, octave, etc.
# Start gnuplot, then from gnuplot prompt
#    set key off # avoid cluttering plots
#    set multiplot layout 1,2
#    plot for [n=2:7] 'greeks.dat' using 1:(column(n)) with lines
#    plot for [n=9:13] 'greeks.dat' using 1:(column(n)) with lines
##     note that column 8 is NaN, because division by 0
#    unset multiplot

# scipy.savetxt('greeks.dat', scipy.column_stack((scipy.transpose(S),
#               scipy.transpose(Delta), scipy.transpose(Gamma))),
#               fmt='%4.3f')

## NAME:  greeks.py
## USAGE: From shell prompt: python3 greeks.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION:  For given parameter values, the Black-Scholes-Merton
## call option "greeks" Delta and Gamma are sampled at a specified
## m X 1 array of times and
## at a specified  1 X n array of security prices using vectorization
## and broadcasting.  The result can be plotted as functions of the
## security price as done in the text.  This approach is taken to
## illustrate the use of vectorization and broadcasting for efficient
## evaluation of an array of solution values from a complicated formula.
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES:  uses scipy and scipy.stats import norm, and matplotlib
## INCOMPATIBILITIES: none known
## PROVENANCE: Created by sdunbar
## BUGS AND LIMITATIONS: No bugs known. 
## The definition of the functions Delta and Gamma does only
## no error checking in the input variables.  This could be improved
## to do type checking and even value checking for appropriate values.
## The calculation of n11, numerd1, d1, denom1 and factor1 uses
## broadcasting, also called
## binary singleton expansion, recycling, single-instruction multiple
## data or replication.
## The calculation is vectorized for an array of S values and an array
## of t values, but it is NOT vectorized for arrays in the parameters
## K, r, T, and sigma.
## The calculation relies on using the rules for calcuation and handling of
## infinity and NaN (Not a Number) which come from divisions by 0, taking
## logarithms of 0, and negative numbers and calculating the normal cdf at
## infinity and negative infinity.  
## The color labeling of the plot lines is the default matplotlib coloring.
## FEATURES AND POTENTIAL IMPROVEMENTS:
## Add a plot key labeling header for the data file used to plot lines.
## The calculation of (for example) matrix d1  requires some analysis because
## it uses the recycling rule.  The vector scipy.log(S/K)  is shape (61,)
## The vector n12 has shape (6,0).  Then use broadcasting to create
## numerd1 of shape (6,61). Finally use broadcasting of division to
## create d1.  This involves division by 0, so a warning is issued.
## To do the plotting. gnuplot plots the columns of greeks.dat
## Delta is 61 rows (one for each time element) by 6 ( one for each t)
## columns, and we wish to plot each row against S which has shape (61,).
## Therefore, it is necessary to take the transpose of Delta.  Likewise for Gamma
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0, as of Wed Dec 31, 2014  7:40 AM
##                  1.1, added graphics, Tue Mar 15, 2016  7:01 AM
## KEYWORDS: Black Scholes equation, Delta, Gamma, greeks

