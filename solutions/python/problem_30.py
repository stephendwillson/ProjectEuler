import math


def main():

    # ceiling = #_digits x 9^exp
    # ceiling = 5 * 9^5 = 295245

    exp = 5
    ceiling = 295245
    total = 0

    # calculate the value of 1 - 9 ^ exp up front to save time
    digit_powers = [math.pow(i, exp) for i in range(10)]

    for i in range(2, ceiling):

        i_total = 0
        for digit in str(i):
            i_total += digit_powers[int(digit)]

        if i_total == i:
            total += i

    return total


if __name__ == "__main__":
    print(main())
