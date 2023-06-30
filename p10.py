"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import extra

import itertools

def main():
    for i in [10, 2_000_000]:
        print(sumOfPrimes(i))
        # 17
        # 142_913_828_922

def sumOfPrimes(limit):
    return sum(itertools.takewhile(lambda n: n < limit, extra.primes()))

main()
