import math
import collections


def main():

    ceiling = 1000
    perimeters = []

    # some algebra magic to narrow down upper bounds significantly
    for a in range(1, ceiling // 4):

        aa = a*a  # calculate part in outer loop to save some time
        for b in range(a, (ceiling - a) // 2 + 1):

            c = math.sqrt(aa + b*b)
            p = a + b + c

            # save perimeter if valid solution is found
            # order of conditions matters a lot for run time
            if p % 2 == 0 and int(p) == p and p <= ceiling:
                perimeters.append(p)

    # the perimeter that shows up the most is the one with the most solutions
    common_p = int(collections.Counter(perimeters).most_common(1)[0][0])

    return common_p


def description():

    desc = """
https://projecteuler.net/problem=39


If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""
    print(desc, end="")


PE_NAME = "PROBLEM NAME"
PE_SOLUTION = 840

if __name__ == "__main__":
    print(main())
