import euler_lib


def main():

    n = 1000 # 2^n

    total = euler_lib.sum_digits(2 ** n)

    return total

def description():

    desc = """
https://projecteuler.net/problem=16

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
"""
    print(desc, end="")

pe_name = "POWER DIGIT SUM"
pe_solution = 1366

if __name__ == "__main__":
    print(main())
