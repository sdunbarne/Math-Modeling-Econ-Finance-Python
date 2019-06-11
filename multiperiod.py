#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scipy

S = 100
factorUp = 1.05
factorDown = 0.95
B = 1
effR = 1.02  # effR = exp(r*delta t_i)
deltati = 1
K = 100


def f(x, strike):  # European call option
    return max(x - strike, 0)


def riskNeutralMeas(fUp, fDown, exprdt):
    return (exprdt - fDown) / (fUp - fDown)  # risk neutral measure pi


piRNM = riskNeutralMeas(factorUp, factorDown, effR)

v11 = 1 / effR * (piRNM * f(S * factorUp * factorUp, K) + (1 - piRNM)
                  * f(S * factorUp * factorDown, K))
v10 = 1 / effR * (piRNM * f(S * factorUp * factorDown, K) + (1 - piRNM)
                  * f(S * factorDown * factorDown, K))

value = 1 / effR * (piRNM * v11 + (1 - piRNM) * v10)

print( 'value:', value, '\n')

## NAME: multiperiod.py
## USAGE: From shell prompt: python3 multiperiod.pl
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: Set up and solve for the
## value of European call option in a
## two period binomial model.
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT:  Python
## DEPENDENCIES: scipy
## INCOMPATIBILITIES: none known
## PROVENANCE: Version 1.0 by sdunbar as of Fri Dec 18, 2015  8:19 AM
## BUGS AND LIMITATIONS: A limitation is that all parameters must be
## entered directly into the script.  Another limitation is that the
## derivative value function is only for a European call option.
## FEATURES AND POTENTIAL IMPROVEMENTS:  Make the script interactive so
## that parameters or the derivative value function can be entered
## from a command line, or through a GUI.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Fri Dec 18, 2015  8:20 AM
##          Version 1.1 as of Tue Mar  1, 2016  7:31 AM, upgrade to python3
## KEYWORDS: two period binomial model, derivative security

