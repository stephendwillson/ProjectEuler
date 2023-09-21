import math


def main():

    # Pre-calculate factorials for 1-9 to save repeated calculations
    # Any 8-digit number has a digits sum of at least 8! = 40,320
    # which is greater than the number itself.
    factorials = [math.factorial(i) for i in range(10)]
    ceiling = 7 * factorials[9]

    total = 0
    for i in range(3, ceiling):

        digit_sum = 0
        num = i
        while num > 0:
            digit_sum += factorials[num % 10]
            num //= 10

        if digit_sum == i:
            total += i

    return total


if __name__ == "__main__":
    print(main())
