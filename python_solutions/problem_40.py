def main():

    ceiling = 1000000

    d = ""
    i = 0
    while len(d) < ceiling:
        i += 1
        d = d + str(i)

    total = int(d[0]) * int(d[9]) * int(d[99]) * int(d[999]) * int(d[9999]) * int(d[99999]) * int(d[999999])

    return total

def description():

    desc = """
https://projecteuler.net/problem=40

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

sdwillso NOTE: 12th digit post-decimal is highlighted in red.
It can be seen that the 12th digit of the fractional part is 1.

If d(n) represents the nth digit of the fractional part, find the value of the following expression.

d(1) × d(10) × d(100) × d(1000) × d(10000) × d(100000) × d(1000000)
"""
    print(desc, end="")

pe_name = "CHAMPERNOWNE'S CONSTANT"
pe_solution = 210

if __name__ == "__main__":
    print(main())
