import math

def main():

    # pre-calc factorial values for each digit
    fact = get_digit_factorials()

    """
    need an upper bound. started by blindly picking 1000000 and it worked.

    tightened further: https://en.wikipedia.org/wiki/Factorion
    
    biggest 7 digit number 9999999 has 7 digit factorial sum much less than self
    biggest 8 digit number 99999999 still has 7 digit factorial sum
    7 * 9! = 2540160
    8 * 9! = 2903040

    any higher than 7 digits is going to have a sum factorials < self
    """
    ceiling = 7 * fact[9]

    total = 0
    for i in range(3, ceiling):
        if i == digit_factorial_sum(i, fact):
            total += i

    return total

# calculate factorials in advance to save time on repeated recalc
def get_digit_factorials():

    return [ 
            math.factorial(0),
            math.factorial(1),
            math.factorial(2),
            math.factorial(3),
            math.factorial(4),
            math.factorial(5),
            math.factorial(6),
            math.factorial(7),
            math.factorial(8),
            math.factorial(9)
            ]

# sum of digits_of_n!
def digit_factorial_sum(n, fact):

    total = 0

    for i in range(0, len(str(n))):        
        total += fact[int(str(n)[i])]

    return total

def description():

    desc = """
https://projecteuler.net/problem=34

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
"""
    print(desc, end="")

pe_name = "DIGIT FACTORIALS"
pe_solution = 40730

if __name__ == "__main__":
    print(main())
