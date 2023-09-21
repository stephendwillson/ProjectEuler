from utils import euler_lib


def main():

    n = 1000000

    total = 0
    for i in range(0, n + 1):

        if euler_lib.is_palindrome(i) and euler_lib.is_palindrome(i, base=2):
            total += i

    return total


if __name__ == "__main__":
    print(main())
