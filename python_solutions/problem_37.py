from utils import euler_lib


def main():

    n = 11

    t_primes = []
    i = 11
    while len(t_primes) < n:

        i += 2

        if euler_lib.is_left_right_truncatable_prime(i):
            t_primes.append(i)

    return sum(t_primes)


if __name__ == "__main__":
    print(main())
