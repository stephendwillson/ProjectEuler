from utils import euler_lib


def main():

    ceiling = 1000000

    # circular prime can't contain these digits because at least one
    # rotation wouldn't be prime
    bad_digits = ['0', '2', '4', '5', '6', '8']

    total = 4  # count single digit primes so they're not excluded...
    for i in range(11, ceiling + 1, 2):  # ...and start loop appropriately

        digit_set = set(str(i))

        if any(digit in digit_set for digit in bad_digits):
            continue

        if euler_lib.is_circular_prime(i):
            total += 1

    return total


if __name__ == "__main__":
    print(main())
