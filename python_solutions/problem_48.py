def main():

    n = 1000

    total = 0
    for i in range(1, n + 1):
        total += i**i

    return int(str(total)[-10:])

def description():

    desc = """
https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
    print(desc, end="")

pe_name = "SELF POWERS"

if __name__ == "__main__":
    print(main())
