"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import extra

import itertools

def main():
    for i in [6, 10_001]:
        print(nthPrimeNumber(i))
        # 13
        # 104_743

def nthPrimeNumber(n):
    return list(itertools.islice(extra.primes(), n))[-1]

main()
