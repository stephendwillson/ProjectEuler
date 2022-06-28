import euler_lib


def main():

    n = 10000
    amicables = list()

    for a in range(1, n):
        
        a_sum = sum(euler_lib.get_proper_factors(a))

        # only add pair once [220, 284] not [220, 284, 284, 220]
        b = a_sum
        if a > b:
            continue
        
        b_sum = sum(euler_lib.get_proper_factors(b))

        if a_sum == b and b_sum == a and a != b:
            amicables.append(a)
            amicables.append(b)

    print("sum of amicable #s below {}: {}".format(n, sum(amicables)))

def description():

    desc = """
https://projecteuler.net/problem=21

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
