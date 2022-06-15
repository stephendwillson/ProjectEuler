"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import sys

test_num = 0
lowest = -1
while lowest == -1:
    # don't need to test any number not ending in 5 or 0
    test_num += 5

    for i in range(1, 21):
        if (test_num % i != 0):
            break
    # triggers if iteration does NOT end in a break
    else:
        lowest = test_num

print("The smallest positive number evenly divisible by 1-20: {}".format(lowest))
