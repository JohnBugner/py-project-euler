"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools

def main():
    for i in [2, 3]:
        print(largestPalindromeOfProductOfTwoNDigitNumbers(i))
        # 9009
        # 906_609

def largestPalindromeOfProductOfTwoNDigitNumbers(n):
    return max(filter(isPalindrome, map(lambda t: t[0] * t[1], itertools.combinations(nDigitNumbers(n), 2))))

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def nDigitNumbers(n):
    return range(10**(n-1), 10**n)

main()
