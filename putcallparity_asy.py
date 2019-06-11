#! /usr/bin/env python3

import scipy

m = 6
n = 61
S0 = 70
S1 = 130 
K = 100
r = 0.12
T = 1.0
sigma = 0.10

time = scipy.linspace(T, 0.0, m)
S = scipy.linspace(S0,S1, n)

logSoverK = scipy.log(S/K)
n12 = ((r + sigma**2/2)*(T-time))
n22 = ((r - sigma**2/2)*(T-time))
numerd1 = logSoverK[scipy.newaxis,:] + n12[:,scipy.newaxis]
numerd2 = logSoverK[scipy.newaxis,:] + n22[:,scipy.newaxis]
d1 = numerd1/(sigma*scipy.sqrt(T-time)[:,scipy.newaxis])
d2 = numerd2/(sigma*scipy.sqrt(T-time)[:,scipy.newaxis])

from scipy.stats import norm
part1 = norm.cdf(-d2) * K*scipy.exp(-r*(T-time))[:,scipy.newaxis]
part2 = S[scipy.newaxis] * norm.cdf(-d1)
VC = part1 - part2

# optional file output to use with external plotting programming
# such as Asymptote

scipy.savetxt('putcallparity_asy.dat',  
    scipy.column_stack((scipy.transpose(S),scipy.transpose(VC))), 
    fmt=('%4.3f'))

## NAME:  putcallparity_asy.py
## USAGE: From shell prompt: python3 solution.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION:  For given parameter values, the Black-Scholes-Merton
## solution formula is sampled at a specified m X 1 array of times and
## at a specified  1 X n array of security prices using vectorization
## and broadcasting.  The result can be plotted as functions of the
## security price as done in the text.  This approach is taken to
## illustrate the use of vectorization and broadcasting for efficient
## evaluation of an array of solution values from a complicated formula.
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: none
## DEPENDENCIES:  uses scipy and scipy.stats import norm
## INCOMPATIBILITIES: none known
## PROVENANCE: Created by sdunbar
## BUGS AND LIMITATIONS: No bugs known, but because I have chosen to
##      NOT use the optional and extra matplotlib graphics packages, the
##      limitation is no plotting or graphical display.
##      To get some graphics, export to an outside utility, including
##      R, octave, or gnuplot.
## The definition of the function VC does only
## no error checking in the input variables.  This could be improved
## to do type checking and even value checking for appropriate values.
## The calculation of n11, n12, numerd1, numerd2, d1 and d2 uses 
## broadcasting, also called
## binary singleton expansion, recycling, single-instruction multiple
## data or replication.
## The calculation is vectorized for an array of S values and an array
## of t values, but it is NOT vectorized for arrays in the parameters
## K, r, T, and sigma.
## The calculation relies on using the rules for calcuation and handling of
## infinity and NaN (Not a Number) which come from divisions by 0, taking
## logarithms of 0, and negative numbers and calculating the normal cdf at
## infinity and negative infinity.  Gnuplot will not plot a NaN which accounts for
## the gap at S = 0 in the graph line for t = 1.
## FEATURES AND POTENTIAL IMPROVEMENTS:
## Add a plot key labeling header for the data file used to plot lines.
## The calculation of the matrices part1 and part2 requires some analysis because
## it uses the recycling rule.  The vector scipy.log(S/K)  is shape (61,)
## The vectors n12, n22 have shape (6,0).  Then use broadcasting to create 
## numerd1 and numerd2 of shape (6,61). Finally use broadcasting of division to 
## create d1 and d2.  This involves division by 0, so a warning is issued.
## Multiply S with norm.cdf(d1) with broadcasting again to get part1
## Multiply K*exp(-r*(T-time)) with norm.cdf(d2) elementwise using braodcasting.
## To do the plotting. Asymptote plots the columns of putcallparity_asy.dat 
## VC is 6 rows (one for each time element) by 61
## columns, and we wish to plot each row against S which has shape (61,).
## Therefore, it is necessary to take the transpose of VC.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0, as of Tue Oct 28 07:24:05 CDT 2014
## KEYWORDS: Black Scholes equation

