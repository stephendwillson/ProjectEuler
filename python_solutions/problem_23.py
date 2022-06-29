import euler_lib


def main():

    ceiling = 28123

    # get all abundant #s under ceiling, stuff into list
    abundant = list()
    for i in range(12, ceiling):
        factors = euler_lib.get_proper_factors(i)

        if sum(factors) > i:
            abundant.append(i)

    # calculate all possible sums once up front; brute force recalcs took ~1100s
    # mark index in array for every possible sum of abundants
    # in the end, any unmarked index is a number that can't be written as a sum of 2 abundants
    sums = [False] * (ceiling + 1)
    for a in abundant:
        for b in abundant:
            
            tmp = a + b
            if tmp >= len(sums):
                break
            sums[tmp] = True

    # add up every index marked True
    total = 0
    for i in range(1, ceiling):
        if sums[i] == False:
            total += i

    return total

def description():

    desc = """
https://projecteuler.net/problem=23

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""
    print(desc, end="")

pe_name = "NON-ABUNDANT SUMS"
pe_solution = 4179871

if __name__ == "__main__":
    print(main())
