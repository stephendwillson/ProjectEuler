from utils import euler_lib


def main():

    # this could be more pythonic, oh well

    n = 0
    while True:
        n += 1

        if (euler_lib.is_permutation(n, 2*n) and 
            euler_lib.is_permutation(n, 3*n) and
            euler_lib.is_permutation(n, 4*n) and
            euler_lib.is_permutation(n, 5*n) and
            euler_lib.is_permutation(n, 6*n)):
                break

    return n


if __name__ == "__main__":
    print(main())
