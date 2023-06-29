"""
2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible
by all of the numbers from 1 to 20?
"""

import functools
import multiset

def main():
    print(smallestNumberDivisibleByNumbers(10)) # 2520
    print(smallestNumberDivisibleByNumbers(20))

def smallestNumberDivisibleByNumbers(limit):
    return product(commonPrimeFactors(range(1, limit + 1)))

def product(xs):
    return functools.reduce(int.__mul__, xs)

def commonPrimeFactors(ns):
    es = multiset.Multiset()

    for e in ns:
        fs = multiset.Multiset(primeFactors(e))
        es.update(fs - es)

    return es

def primeFactors(n):
    ds = []

    while n % 2 == 0:
        ds.append(2)
        n /= 2

    if True:
        d = 3

        while d <= n:
            while n % d == 0:
                ds.append(d)
                n /= d

            d += 2

    return ds

main()
