import math


def main():

    ceiling = 1000000

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

    permutation = []
    length = len(digits)

    for _ in range(length):

        # calculate the factorial for the remaining digits
        factorial = math.factorial(length - 1)

        # calculate the index of the digit to add to the permutation
        index = (ceiling - 1) // factorial

        # add the digit to the permutation and remove from the list of digits
        digit = digits[index]
        permutation.append(digit)
        digits.remove(digit)

        # adjust the ceiling and length for the next iteration
        ceiling = ceiling - (index * factorial)
        length = length - 1

    nth_permutation = int("".join(str(d) for d in permutation))

    return nth_permutation


if __name__ == "__main__":
    print(main())
