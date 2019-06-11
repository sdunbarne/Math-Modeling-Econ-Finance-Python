#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scipy
from scipy import linalg

S = 50
up = .10
down = 0.03
B = 1
r = 0.06
T = 1
K = 50


def f(x, strike):
    return max(x - strike, 0)


m = scipy.array([[S * (1 - down), B * scipy.exp(r * T)], [S * (1 + up),
                B * scipy.exp(r * T)]])
payoff = scipy.array([f(S * (1 - down), K), f(S * (1 + up), K)])

portfolio = scipy.linalg.solve(m, payoff)
value = scipy.vdot(portfolio, scipy.array([S, B]))

print( 'portfolio: phi=', portfolio[0], 'psi=', portfolio[1], '\n')
print( 'derivative value: ', value, '\n')

## NAME:  singleperiod.py
## USAGE: From shell prompt: python3 singleperiod.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Set up and solve for the replicating portfolio
## and the value of the corresponding derivative security in a
## single period binomial model.
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT:
## DEPENDENCIES: Scientific python
## INCOMPATIBILITIES: none known
## PROVENANCE: version 1.0 by sdunbar as of Mon Dec 14, 2015  5:54 AM
## BUGS AND LIMITATIONS: A limitation is that all parameters must be
## entered directly into the script.
## FEATURES AND POTENTIAL IMPROVEMENTS:  Make the script interactive so
## that parameters can be entered from a command line, perhaps as a function,
## or through a GUI.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Mon Dec 14, 2015  5:54 AM
##          Version 1.1 as of Tue Mar  1, 2016  7:31 AM, upgrade to python3
## KEYWORDS:  single period biomial model, derivative security, replicating portfolio
