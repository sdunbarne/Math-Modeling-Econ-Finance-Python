#! /usr/bin/env python3
import scipy

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

m1 = N/5
partition1 = scipy.linspace( 0, T, m1+1)
m2 = N
partition2 = scipy.linspace( 0, T, m2+1)
m3 = 3*N
partition3 = scipy.linspace( 0, T, m3+1)

qv1 = scipy.sum( (WcaretN( partition1[1:m1+1] ) - WcaretN(partition1[0:m1] ) )**2)
qv2 = scipy.sum( (WcaretN( partition2[1:m2+1] ) - WcaretN(partition2[0:m2] ) )**2)
qv3 = scipy.sum( (WcaretN( partition3[1:m3+1] ) - WcaretN(partition3[0:m3] ) )**2)

print( "Quadratic variation of approximation of  Wiener process paths with ", N, "scaled random steps with ", m1, "partition intervals is: ", qv1)
print( "Quadratic variation of approximation of  Wiener process paths with ", N, "scaled random steps with ", m2, "partition intervals is: ", qv2)
print( "Quadratic variation of approximation of  Wiener process paths with ", N, "scaled random steps with ", m3, "partition intervals is: ", qv3)

## NAME: quadraticvariation.py
## USAGE: From shell prompt: python3 quadraticvariation.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: 
##   Using a scaled random walk approximation of the Wiener process,
##   find the quadratic variation on 3 different partitions of [0,T],
##   the first a factor of N, the second N itself, the third a multiple of N.
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: none
## DEPENDENCIES: none
## INCOMPATIBILITIES: None known
## PROVENANCE: Created by sdunbar
## BUGS AND LIMITATIONS: None known
## FEATURES AND POTENTIAL IMPROVEMENTS:
##   The quadratic variation calculation takes advantage of the design of
##   WcaretN as vector-capable, that is, the input can be
##   a vector or array, and the output will be a vector of values of the 
##   approximation function at the corresponding points.
##   Because the quadratic variaiotn is computed using the scaled random
##   walk approximation of the Wiener process, the quadratic variation will be
##   1/k for a multiple k of N.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Mon Aug  5, 2013  5:40 AM
## KEYWORDS: random walk, Wiener process, Brownian motion, quadratic variation


