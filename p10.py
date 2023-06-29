"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import math

def main():
    print(sumOfPrimes(10)) # 17
    print(sumOfPrimes(2_000_000))

def sumOfPrimes(limit):
    return sum(primes(limit))

def primes(limit):
    ns = [2,3]

    while True:
        n = ns[-1] + 2

        while True:
            if isPrime(n):
                break
            else:
                n += 2

        if n < limit:
            ns.append(n)
        else:
            break

    return ns

def isPrime(n):
    if n <= 1:
        return False
    else:
        return not(any(map(lambda d: n % d == 0, [2] + list(range(3, math.isqrt(n) + 1, 2)))))

main()
