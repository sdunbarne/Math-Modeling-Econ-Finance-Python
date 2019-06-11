#! /usr/bin/env python3

import scipy

mu = 1.;
sigma = 0.5;
T = 1.
# length of the interval [0, T] in time units

trials = 200
N = 100
# number of end-points of the grid including T
Delta = T/N;
# time increment

W = scipy.zeros((trials, N+1), dtype = float)
# initialization of the vector W approximating
# Wiener process
t = scipy.ones( (trials,N+1), dtype = float) * scipy.linspace(0, T, N+1)
# Note the use of recycling
W[:, 1:N+1] = scipy.cumsum(scipy.sqrt(Delta)*scipy.random.standard_normal( (trials, N)), axis = 1,)

GBM = scipy.exp( mu*t + sigma*W)
meanGBM = scipy.mean(GBM, axis=0)
predicted_mean_GBM_rate = mu + (1./2.)*sigma**2

meanGBM_rate = scipy.polyfit( scipy.linspace(0, T, N+1), scipy.log(meanGBM), 1)

print( "Observed Mean GBM Relative Rate:", meanGBM_rate[0]);
print( "Predicted Mean GBM Relative Rate:", predicted_mean_GBM_rate);

## NAME: geometricbrownian.py
## USAGE: From shell prompt: python3 geometricbrownian.py
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: create \verb+ trials + sample paths of Geometric
## Brownian Motion, sampled at \( N \) equally-spaced values on \(
##  [0,T]\).
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: none
## DEPENDENCIES: none
## INCOMPATIBILITIES: none known
## PROVENANCE: created by sdunbar
## BUGS AND LIMITATIONS: none known
## FEATURES AND POTENTIAL IMPROVEMENTS:
##  The function assumes the inputs and parameters are sensible.
##  Better input checking could catch errors before calculating.

## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Mon Jul 14, 2014  7:45 AM
## KEYWORDS: Weiner process, Brownian Motion, Geometric Brownian
## Motion, relative growth rate


