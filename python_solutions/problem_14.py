import euler_lib


def main():
    
    n = 1000000

    longest = 0
    start_num = 0

    for i in range(1, n + 1):
        
        tmp = euler_lib.get_collatz_length(i)

        if tmp > longest:
            longest = tmp
            start_num = i

    return start_num

def description():

    desc = """
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
    print(desc, end="")
pe_name = "LONGEST COLLATZ SEQUENCE"
if __name__ == "__main__":
    main()
