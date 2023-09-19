from utils import euler_lib


def main():

    ceiling = 28123

    # get all abundant #s under ceiling, stuff into list
    abundant = []
    for i in range(12, ceiling):
        factors = euler_lib.get_proper_factors(i)
        if sum(factors) > i:
            abundant.append(i)

    # calculate all possible sums up front
    # mark index in list for every possible sum of abundants
    # any unmarked index is number that can't be written as sum of 2 abundants
    sums = [False] * (ceiling + 1)
    for i, x in enumerate(abundant):
        for y in abundant[i:]:
            tmp = x + y
            if tmp > ceiling:
                break
            sums[tmp] = True

    # add up every index marked False
    total = 0
    for i in range(1, ceiling+1):
        if not sums[i]:
            total += i

    return total


if __name__ == "__main__":
    print(main())
