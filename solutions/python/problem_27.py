from utils import euler_lib


def main():

    max_a = 1000
    max_b = 1000

    # compute the list of odd primes up to the max value of b
    tmp_prime_list = euler_lib.get_primes_below_n(max_b)
    prime_list = []
    for p in tmp_prime_list:
        if 2 < p < max_b and p % 2 == 1:
            prime_list.append(p)

    max_prime_seq_len = 0
    max_product = 0

    for a in range(-max_a, max_a + 1):
        for b in prime_list:

            # count number of consecutive primes
            n = 1
            while euler_lib.is_prime(n*n + a*n + b):
                n += 1

            if n > max_prime_seq_len:
                max_prime_seq_len = n
                max_product = a * b

    return max_product


if __name__ == "__main__":
    print(main())
