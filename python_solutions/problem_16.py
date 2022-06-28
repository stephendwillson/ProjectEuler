import euler_lib


def main():

    n = 1000 # 2^n

    total = euler_lib.sum_digits(2 ** n)
    print("sum: {}".format(total))

def description():

    desc = """
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
