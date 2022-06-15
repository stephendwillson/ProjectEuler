"""
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import sys

highest = -1
end_i = -1
end_j = -1
for i in range(1,1000):
    for j in range(1,1000):
        product = i * j
        # cast as a string and compare front to back
        if (str(product) == str(product)[::-1]):
            end_i = i
            end_j = j
            if (product > highest):
                highest = product

print("The largest palindrome from the product of two 3-digit numbers: {}".format(highest))
print("This is the product of {} x {}".format(end_i, end_j))
