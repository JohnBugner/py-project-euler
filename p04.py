"""
A palindromic number reads the same both ways.
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import itertools

def main():
    print(largestPalindromeOfProductOfTwoNDigitNumbers(2)) # 9009
    print(largestPalindromeOfProductOfTwoNDigitNumbers(3))

def largestPalindromeOfProductOfTwoNDigitNumbers(n):
    return max(filter(isPalindrome, map(lambda t: t[0] * t[1], itertools.combinations(_NDigitNumbers(n), 2))))

def isPalindrome(n):
    return str(n) == str(n)[::-1]

def _NDigitNumbers(n):
    return range(10**(n-1), 10**n)

main()
