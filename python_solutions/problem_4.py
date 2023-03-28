def main():

    palindromes = []

    for i in range(1, 1000):
        for j in range(1, 1000):
            prod = i * j

            if str(prod) == str(prod)[::-1]:
                palindromes.append(prod)

    return max(palindromes)


def description():

    desc = """
https://projecteuler.net/problem=4

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
    print(desc, end="")


PE_NAME = "LARGEST PALINDROME PRODUCT"
PE_SOLUTION = 906609

if __name__ == "__main__":
    print(main())
