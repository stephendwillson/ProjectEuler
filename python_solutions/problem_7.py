from utils import euler_lib


def main():

    num_primes = 10001

    return get_nth_prime(num_primes)


def get_nth_prime(n):

    count = 0
    i = 0

    while count < n:
        i += 1
        if euler_lib.is_prime(i):
            count += 1

    return i


if __name__ == "__main__":
    print(main())
