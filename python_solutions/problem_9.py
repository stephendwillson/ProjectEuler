"""
https://projecteuler.net/problem=9

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import time

def main():

    start_time = time.process_time()
    triplet = brute_force()
    end_time = time.process_time()
    print("Time taken for brute force: {}".format(end_time - start_time))

    start_time = time.process_time()
    triplet = optimized()
    end_time = time.process_time()
    print("Time taken for square sum relation solution: {}".format(end_time - start_time))

    # convert list to int for math.prod
    triplet = [int(i) for i in triplet]

    if (triplet is None):
        print("Triplet not found. This shouldn't trigger.")
        exit(-1)
    
    # convert list to int for math.prod
    triplet = [int(i) for i in triplet]

    print("Pythagorean triplet satisfying a + b + c = 1000: {}".format(triplet))
    print("Product of triplet is {}".format(math.prod(triplet)))

def brute_force():
 
    for a in range(0, 1000):
        for b in range(0, 1000):
            for c in range(0, 1000):

                if (a < b and b < c and
                    a + b + c == 1000 and
                    a*a + b*b == c*c):
                    return [a, b, c]          

    return None

# square sum relation: (a^2 + b^2 = c^2) == (c^2 = m^4 + n^4 + 2*m^2*n^2)
def optimized():

    c = 0
    m = 0

    while True:
        for n in range(1, m):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n

            if (a + b + c == 1000):
                return [a, b, c]

        m += 1

    return None

main()
