#! /usr/bin/env python3

import scipy

from scipy.stats import norm

def f(sigma, S, K, r, Tminust, C):
    logSoverK = scipy.log(S/K)
    n12 = ((r + sigma**2/2)*Tminust)
    n22 = ((r - sigma**2/2)*Tminust)
    numerd1 = logSoverK + n12
    numerd2 = logSoverK + n22
    d1 = numerd1/(sigma*scipy.sqrt(Tminust))
    d2 = numerd2/(sigma*scipy.sqrt(Tminust))
    part1 = norm.cdf(d1) * S
    part2 = K*scipy.exp(-r*(Tminust)) * norm.cdf(d2)
    VC = part1 - part2
    return VC - C

def fprime(sigma, S, K, r, Tminust, C):
    logSoverK = scipy.log(S/K)
    n12 = ((r + sigma**2/2)*Tminust)
    numerd1 = logSoverK + n12
    d1 = numerd1/(sigma*scipy.sqrt(Tminust))
    return S*scipy.sqrt(Tminust)*norm.pdf(d1)*scipy.exp(-r*Tminust)

S = 21.
K = 20.
Tminust = 0.25
r = 0.10
C = 1.85

sigmaNew = 0.20
epsilon = 10.**(-5)

while( True ):
    sigmaOld = sigmaNew
    sigmaNew = sigmaOld - f(sigmaOld, S, K, r, Tminust, C)/fprime(sigmaOld, S, K, r, Tminust, C) 
    if ( scipy.absolute( sigmaNew - sigmaOld ) < epsilon ):
        break

print( sigmaNew )

## NAME: impliedvolatility.py
## USAGE: From shell prompt: python3 solution.py
##        or within interactive python3 environment, import filename
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION:
## For given numerical values for \( \sigma_0 \), the guess for
## the volatility; \( S \), the currect security price; \( K \),
## the strike price; \( r \), the risk-free interest rate; \( T -
## t \), the time to expiration; and \( C \), the current call
## option price, the script uses Newton's method to find the implied
## volatility with error tolerance \( \epsilon \).
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: none
## DEPENDENCIES: none
## INCOMPATIBILITIES: none known
## PROVENANCE: Created by sdunbar
## BUGS AND LIMITATIONS: 
## FEATURES AND POTENTIAL IMPROVEMENTS:
## Modify the scripts for implied volatility to be a function which
## takes the numerical values for \( \sigma_0 \), the guess for
## the volatility; \( S \), the currect security price; \( K \),
## the strike price; \( r \), the risk-free interest rate; \( T -
## t \), the time to expiration; and \( C \), the current call
## option price.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0, as of Wed Dec 17, 2014  5:56 AM
## KEYWORDS: Black Scholes equation, implied volatility, Newton's method


