"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import extra

def main():
    for i in [49, 13_195, 600_851_475_143]:
        print(largestPrimeFactor(i))
        # 7
        # 29
        # 6857

def largestPrimeFactor(n):
    return max(extra.primeFactors(n))

main()
