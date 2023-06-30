"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

import extra

import multiset

def main():
    for i in [10, 20]:
        print(smallestNumberDivisibleByNumbers(i))
        # 2520
        # 232_792_560

def smallestNumberDivisibleByNumbers(limit):
    return extra.product(commonPrimeFactors(range(1, limit + 1)))

def commonPrimeFactors(ns):
    es = multiset.Multiset()

    for e in ns:
        fs = multiset.Multiset(extra.primeFactors(e))
        es.update(fs - es)

    return es

main()
