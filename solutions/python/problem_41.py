from utils import euler_lib


def main():

    # if the sum of a number's digits is divisible by 3, the number is divisible by 3
    # 8 and 9 digit numbers can then be skipped here
    # 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 == 45
    # instead, start from the biggest 7 digit pandigital number
    ceiling = 7654321
    high = -1

    for n in range(ceiling, 1, -1):
        if n % 2 == 0:
            continue
        if n > high and euler_lib.is_pandigital(n) and euler_lib.is_prime(n):
            high = n
            break

    return high

if __name__ == "__main__":
    print(main())