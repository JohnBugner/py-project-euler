"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

import extra

def main():
    print(largestPrimeFactor(49)) # 7
    print(largestPrimeFactor(13_195)) # 29
    print(largestPrimeFactor(600_851_475_143))

def largestPrimeFactor(n):
    return max(extra.primeFactors(n))

main()
