"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which

    a^2 + b^2 = c^2.

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import extra

import itertools

def main():
    print(productsOfPythagoreanTriplesWithSumOfN(12)) # 60
    print(productsOfPythagoreanTriplesWithSumOfN(1000))

def productsOfPythagoreanTriplesWithSumOfN(n):
    a = list(itertools.combinations(range(1, n), 3))
    b = list(filter(lambda triple: sum(triple) == n, a))
    c = list(filter(isPythagoreanTriple, b))
    d = list(map(extra.product, c))
    return d

def isPythagoreanTriple(triple):
    return triple[0]**2 + triple[1]**2 == triple[2]**2

main()
