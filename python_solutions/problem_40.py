def main():

    ceiling = 1000000

    # starting with a list and converting to string afterward runs
    # significantly faster than if we begin with a string
    d = []
    i = 0
    while len(d) < ceiling:
        i += 1
        d.append(str(i))

    d = ''.join(d)

    total = (
        int(d[0])
        * int(d[9])
        * int(d[99])
        * int(d[999])
        * int(d[9999])
        * int(d[99999])
        * int(d[999999])
    )

    return total


def description():

    desc = """
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive
integers:

0.123456789101112131415161718192021...

sdwillso NOTE: 12th digit post-decimal is highlighted in red.
It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part, find the value of the
following expression.

d(1) x d(10) x d(100) x d(1000) x d(10000) x d(100000) x d(1000000)
"""
    print(desc, end="")


PE_NAME = "CHAMPERNOWNE'S CONSTANT"
PE_SOLUTION = 210

if __name__ == "__main__":
    print(main())
