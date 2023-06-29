"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import extra

import itertools

def main():
    print(sumOfPrimes(10)) # 17
    print(sumOfPrimes(2_000_000))

def sumOfPrimes(limit):
    return sum(itertools.takewhile(lambda n: n < limit, extra.primes()))

main()
