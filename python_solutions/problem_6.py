"""
https://projecteuler.net/problem=6

The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is,
3025 - 385 = 2640

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def main():

    n = 100

    summed = sum_of_squares(n)
    squared = square_of_sums(n)
    delta = squared - summed

    print("Sum of squares: {}".format(summed))
    print("Square of sums: {}".format(squared))
    print("Delta: {} - {} = {}".format(squared, summed, delta))

def sum_of_squares(n):
    
    total = 0
    for i in range(1, n + 1):
        total += i * i

    return total

def square_of_sums(n):
    
    total = 0
    for i in range(1, n + 1):
        total += i

    return total * total

main()
