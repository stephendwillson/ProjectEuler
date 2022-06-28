import itertools

def main():

    n = 1000000
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    permutations = list(itertools.permutations(digits))
    permutations.sort()

    nth_permutation = "".join(str(p) for p in permutations[n - 1])
    print("permutation #{}: {}".format(n, nth_permutation))

def description():

    desc = """
https://projecteuler.net/problem=24

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
