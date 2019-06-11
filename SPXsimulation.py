#!/usr/bin/python3
# -*- coding: utf-8 -*-

import scipy
from scipy.stats import norm

n = 10000

S = 1614.96  # Standard and Poors 500 Index, on 07/01/2013
r = 0.008  # implied risk free interest rate, between 3 year and 5 year T-bill rate
sigma = 0.1827  # implied volatility
K = 1575  # strike price
Tminust = 110. / 365.  # 07/01/2013 to 10/19/2013

numerd1 = scipy.log(S / K) + (r + sigma ** 2 / 2) * Tminust
numerd2 = scipy.log(S / K) + (r - sigma ** 2 / 2) * Tminust
d1 = numerd1 / (sigma * scipy.sqrt(Tminust))
d2 = numerd2 / (sigma * scipy.sqrt(Tminust))
part1 = S * (norm.cdf(d1) - 1)
part2 = K * scipy.exp(-r * Tminust) * (norm.cdf(d2) - 1)
VP = part1 - part2

x = norm.rvs(size=n)
y1 = scipy.maximum(0, K - S * scipy.exp((r - sigma ** 2 / 2) * Tminust
                   + sigma * x * scipy.sqrt(Tminust)))
y2 = scipy.maximum(0, K - S * scipy.exp((r - sigma ** 2 / 2) * Tminust
                   + sigma * -x * scipy.sqrt(Tminust)))
y = (y1 + y2) / 2

from scipy.stats import expon
u = expon.rvs(size=n, scale=1. / 0.5)
tildeg = (scipy.maximum(0, K - S * scipy.exp((r - sigma ** 2 / 2)
          * Tminust - sigma * scipy.sqrt(Tminust) * scipy.sqrt(u)))
          + scipy.maximum(0, K - S * scipy.exp((r - sigma ** 2 / 2)
          * Tminust + sigma * scipy.sqrt(Tminust) * scipy.sqrt(u)))) \
    / scipy.sqrt(2 * scipy.pi * u)


def ttest(data, confidence=0.95):
    m = scipy.mean(data)
    se = scipy.stats.sem(data)
    df = len(data) - 1
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., df)
    return (m, m - h, m + h)


[mc100mu, mc100cil, mc100cir] = ttest(scipy.exp(-r * Tminust)
        * y1[0:99], 0.95)
[mc1000mu, mc1000cil, mc1000cir] = ttest(scipy.exp(-r * Tminust)
        * y1[0:999], 0.95)
[mcallmu, mcallcil, mcallcir] = ttest(scipy.exp(-r * Tminust) * y1,
        0.95)

[anti100mu, anti100cil, anti100cir] = ttest(scipy.exp(-r * Tminust)
        * y[0:99], 0.95)
[anti1000mu, anti1000cil, anti1000cir] = ttest(scipy.exp(-r * Tminust)
        * y[0:999], 0.95)
[antiallmu, antiallcil, antiallcir] = ttest(scipy.exp(-r * Tminust)
        * y, 0.95)

[imp100mu, imp100cil, imp100cir] = ttest(scipy.exp(-r * Tminust)
        * tildeg[0:99], 0.95)
[imp1000mu, imp1000cil, imp1000cir] = ttest(scipy.exp(-r * Tminust)
        * tildeg[0:999], 0.95)
[impallmu, impallcil, impallcir] = ttest(scipy.exp(-r * Tminust)
        * tildeg, 0.95)

putestimate = [
    VP,
    mc100mu,
    mc1000mu,
    mcallmu,
    anti100mu,
    anti1000mu,
    antiallmu,
    imp100mu,
    imp1000mu,
    impallmu,
    ]
putconfintleft = [
    scipy.nan,
    mc100cil,
    mc1000cil,
    mcallcil,
    anti100cil,
    anti1000cil,
    antiallcil,
    imp100cil,
    imp1000cil,
    impallcil,
    ]
putconfintright = [
    scipy.nan,
    mc100cir,
    mc1000cir,
    mcallcir,
    anti100cir,
    anti1000cir,
    antiallcir,
    imp100cir,
    imp1000cir,
    impallcir,
    ]
d = scipy.transpose(scipy.array([putestimate, putconfintleft,
                    putconfintright]))

print(d)

## NAME: SPXsimulation.py
## USAGE: From shell prompt: python3 SPXsimulation.py
##        or within interactive python3 environment, scrape and past
## REQUIRED ARGUMENTS: none
## OPTIONS: none
## DESCRIPTION: The purpose of this script is to calculate the value of a put option
## on the Standard & Poors 500 stock index (SPX).   First
## the script uses the Black Scholes formula for a put option to calculate the
## theoretical value for a put option.  Then the script uses Monte Carlo
## simulation based on the Geometric Brownian Motion with the SPX
## parameters to find an estimate for the put option value.  Finally, the script
## uses Monte Carlo simulation with antithetic sampling and importance sampling
## variance reduction methods to refine the estimates.  The ultimate purpose
## is to compare the various Monte Carlo methods with the actual put option value.
## DIAGNOSTICS: none
## CONFIGURATION AND ENVIRONMENT: python
## DEPENDENCIES: uses scipy and scipy.stats import norm
## INCOMPATIBILITIES: none known
## PROVENANCE: created by sdunbar
## BUGS AND LIMITATIONS: none known
## FEATURES AND POTENTIAL IMPROVEMENTS:
## SPX data is from: https://www.historicaloptiondata.com/
## Interest rates are from http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Pages/TextView.aspx?data=yieldYear&year=2013
## Profiling with python -m profile -s time reveals no obvious hotspots within the
## script, total running time on my set up is 0.441 seconds.
## AUTHOR:  Steve Dunbar
## VERSION: Version 1.0 as of Thu Aug 27, 2015 10:31 AM
##          Version 1.1 as of Fri Jan 22, 2016  7:24 AM, added present
##                      value discounting to correct the calculations.
## KEYWORDS: Monte Carlo simulation, put option, Geometric Brownian
## Motion, variance reduction, antithetic sampling, importance sampling
