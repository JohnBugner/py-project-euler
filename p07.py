"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
we can see that the 6th prime is 13.

What is the 10001st prime number?
"""

import math

def main():
    print(primes(6)[-1]) # 13
    print(primes(10_001)[-1])

def primes(indexLimit):
    ns = [2,3]

    while len(ns) < indexLimit:
        n = ns[-1] + 2

        while True:
            if isPrime(n):
                ns.append(n)
                break
            else:
                n += 2

    return ns

def isPrime(n):
    if n <= 1:
        return False
    else:
        return not(any(map(lambda d: n % d == 0, [2] + list(range(3, math.isqrt(n) + 1, 2)))))

main()
