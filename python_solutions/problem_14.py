def main():

    ceiling = 1000000

    # create cache
    lengths_cache = [-1] * ceiling
    lengths_cache[1] = 1

    max_length = 0
    max_length_n = 0
    for i in range(2, ceiling):
        n = i
        seq_length = 0

        while n > 1:

            # if we get cache hit, add number to current length and bail out
            if n < i and lengths_cache[n] != -1:
                seq_length += lengths_cache[n]
                break

            # collatz
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n + 1

            seq_length += 1

        # update cache
        lengths_cache[i] = seq_length

        if seq_length > max_length:
            max_length = seq_length
            max_length_n = i

    return max_length_n


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
