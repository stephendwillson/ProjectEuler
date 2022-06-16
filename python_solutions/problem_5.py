"""
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

import time

def main():

    n = 0
    low = 0
    
    start_time = time.process_time()

    while not low:
        n += 20
        for i in range(1, 21):
            if (n % i != 0):
                break
        else:
            low = n
    
    end_time = time.process_time()
    print("time to find solution: {}".format(end_time - start_time))
    print("smallest number divisible by 1-20: {}".format(low))

main()
