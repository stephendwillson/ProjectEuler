"""
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

def main():

    n = 1000 # 2^n

    exp = get_exp(n)

    total = sum_digits(exp)
    print("sum: {}".format(total))

def get_exp(n):

    return 2 ** n

def sum_digits(n):

    total = 0

    for digit in str(n):
        total += int(digit)

    return total


main()
