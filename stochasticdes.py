#! /usr/bin/env python3

import scipy
import matplotlib.pyplot as plt

r = -1.			# growth/decay rate
sigma = 0.5		# standard deviation
b = 3.			# initial value

M = 100			# number of steps for EM method to take
T = 1.			# maximum time, note type real
h = T/M			# time step
t = scipy.linspace(0,T,M+1) # vector of [0, 1h, 2h, 3h...Nh]
X = scipy.zeros( M + 1 )

N = 30*(M+1)		# number of steps for the Brownian Motion

# the random walk
p = 0.5
S = scipy.zeros(N+1)
S[1:N+1] = scipy.cumsum( 2*( scipy.random.random(N) <= p ) - 1 )

def WcaretN(x):
    Delta = T/N                 # T real coerces Delta real
    prior = scipy.floor(x/Delta).astype(int)
    subsequent = scipy.ceil(x/Delta).astype(int)
    return scipy.sqrt(Delta)*(S[prior] + (x/Delta - prior)*(S[subsequent] - S[prior]))

X[0] = b                        # iniital value at t = 0
for i in range(0,M):
    X[i+1] = X[i]+r*X[i]*h+sigma*X[i]*( WcaretN(t[i]+h)-WcaretN(t[i]) )

plt.plot(t,X)
plt.xlabel('t')
plt.ylabel('X')
plt.title('r=-1, sigma=0.5, steps=100')
plt.show()

# optional file output to use with external plotting programming
# such as gnuplot, R, octave, etc. 
# Start gnuplot, then from gnuplot prompt
#    plot "stochasticdes.dat" with lines
# f = open('stochasticdes.dat', 'w')
# for j in range(0,M+1):
#     f.write( str(t[j])+' '+str(X[j])+'\n');

# f.close()

## NAME: stochasticdes.py
## USAGE: From shell prompt: python3 stochasticdes.py
##         or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Simulation of solution of linear stochastic 
## differential equations using the Euler-Maruyama Method
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: requires matplotlib
## DEPENDENCIES:  requires matplotlib
## INCOMPATIBILITIES: none known
## PROVENANCE: Created by sdunbar,
## BUGS AND LIMITATIONS: No bugs known.
## FEATURES AND POTENTIAL IMPROVEMENTS:  An improvement is to add in a
##   graphics package, probably the matplotlib
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Wed Jun  4, 2014  5:49 AM
##          Version 1.1 as of Fri Mar 11, 2016  7:34 AM
## KEYWORDS: stochastic differential equations, Euler-Maruyama method
## Wiener process


