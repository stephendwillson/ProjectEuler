from utils import euler_lib

def main():

    n = 600851475143

    factors = euler_lib.get_prime_factors(n)

    return max(factors)

if __name__ == "__main__":
    print(main())
