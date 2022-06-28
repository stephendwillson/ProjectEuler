def main():

    n = 1000

    total = 0
    for i in range(1, n + 1):
        total += i**i

    print("last 10 digits for n={}: {}".format(n, str(total)[-10:]))

def description():

    desc = """
https://projecteuler.net/problem=48

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
