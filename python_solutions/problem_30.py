def main():

    # x ^ n
    n = 5

    """
    need an upper bound. started by blindly picking 1000000 and it worked.
    
    tightened further, n is 5, number of digits must be at least 5
    
    ceiling = #_digits x 9^n 
    ceiling = 5 * 9^5
    ceiling = 295245
    """
    ceiling = 295245

    total = 0

    # 1 doesn't count per rules so start at 2
    for i in range(2, ceiling):
        tmp = digit_to_power(i, n)
        if tmp == i:
            total += i
    
    print("sum: {}".format(total))

# sum of digits_of_n ^ exp
def digit_to_power(n, exp):

    total = 0

    for i in range(0, len(str(n))):
        
        digit = int(str(n)[i])
        total += digit ** exp

    return total

def description():

    desc = """
https://projecteuler.net/problem=30

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""
    print(desc, end="")

if __name__ == "__main__":
    main()
