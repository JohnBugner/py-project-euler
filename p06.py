"""
The sum of the squares of the first ten natural numbers is,

    1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,

    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the
first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the
first one hundred natural numbers and the square of the sum.
"""

import extra

def main():
    for i in [10, 100]:
        print(diffBetweenSquareOfSumsAndSumOfSquares(i))
        # 2640
        # 25_164_150

def diffBetweenSquareOfSumsAndSumOfSquares(limit):
    return squareOfSums(limit + 1) - sumOfSquares(limit + 1)

def squareOfSums(limit):
    return extra.square(sum(range(1, limit)))

def sumOfSquares(limit):
    return sum(map(extra.square, range(1, limit)))

main()
