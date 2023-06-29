"""
If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def main():
    print(sumOfMultiplesOf3Or5(10)) # 23
    print(sumOfMultiplesOf3Or5(1000))

def sumOfMultiplesOf3Or5(limit):
    return sum(filter(isMultipleOf3Or5, range(limit)))

def isMultipleOf3Or5(n):
    return (n % 3 == 0) or (n % 5 == 0)

main()
