from utils import euler_lib


def main():

    n = 10000
    amicables = []

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

    return sum(amicables)


if __name__ == "__main__":
    print(main())
