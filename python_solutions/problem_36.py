"""
https://projecteuler.net/problem=36

The decimal number, 585 = 1001001001,2 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import euler_lib


n = 1000000

total = 0
for i in range(0, n + 1):
    
    i_b = bin(i).replace("0b", "")
    if euler_lib.is_palindrome(i) and euler_lib.is_palindrome(i_b):
        total += i

print("sum of all base 2/base 10 palindromes under {}: {}".format(n, total))
