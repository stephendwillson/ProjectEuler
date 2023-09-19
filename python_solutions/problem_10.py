from utils import euler_lib


def main():

    ceiling = 2000000

    primes = euler_lib.get_primes_below_n(ceiling)

    return sum(primes)


if __name__ == "__main__":
    print(main())
