import functools
import math

# oeis.org/A000045
def fibonaccis():
    ns = [0,1]
    yield 0
    yield 1

    while True:
        n = ns[-2] + ns[-1]
        ns.append(n)
        yield n

def isEven(n):
    return n % 2 == 0

def isPrime(n):
    if n <= 1:
        return False
    else:
        return not(any(map(lambda d: n % d == 0, [2] + list(range(3, math.isqrt(n) + 1, 2)))))

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

def primes():
    ns = [2]
    yield 2

    n = 3
    while True:
        if isPrime(n):
            ns.append(n)
            yield n

        n += 2

def product(xs):
    return functools.reduce(int.__mul__, xs)

def square(n):
    return n * n

def windows(xs, length):
    return [xs[i:i+length] for i in range(len(xs)-length+1)]
