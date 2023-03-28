def main():

    ceiling = 1000000

    # naive approach took too long, so now cache collatz lengths
    lengths = [0] * ceiling

    for origin in range(1, ceiling + 1):

        n = origin
        length = 0
        while True:

            # if no cache hit found, update cache
            if n == 1:
                lengths[origin-1] = length
                break

            # if cache hit found, stop calc and update cache
            if n <= len(lengths) and lengths[n-1] != 0:
                lengths[origin-1] = lengths[n-1] + length
                break

            # collatz
            if n % 2 == 0:
                n = n//2
            else:
                n = 3*n + 1

            length += 1

    highest = lengths.index(max(lengths)) + 1

    return highest


def description():

    desc = """
https://projecteuler.net/problem=14

The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

It can be seen that this sequence (starting at 13 and finishing at 1) contains
10 terms. Although it has not been proved yet (Collatz Problem), it is thought
that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""
    print(desc, end="")


PE_NAME = "LONGEST COLLATZ SEQUENCE"
PE_SOLUTION = 837799

if __name__ == "__main__":
    print(main())
