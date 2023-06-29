"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?
"""

def main():
    print(largestPrimeFactor(49)) # 7
    print(largestPrimeFactor(13_195)) # 29
    print(largestPrimeFactor(600_851_475_143))

def largestPrimeFactor(n):
    return max(primeFactors(n))

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
