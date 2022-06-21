"""
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""

import euler_lib


n = 1000 # 2^n

total = euler_lib.sum_digits(2 ** n)
print("sum: {}".format(total))
