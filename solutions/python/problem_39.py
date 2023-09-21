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


if __name__ == "__main__":
    print(main())
