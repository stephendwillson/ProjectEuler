def main():

    n = 0
    low = 0
        
    while not low:
        n += 20
        for i in range(1, 21):
            if n % i != 0:
                break
        else:
            low = n    

    return low

def description():

    desc = """
https://projecteuler.net/problem=5

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""
    print(desc, end="")
pe_name = "SMALLEST MULTIPLE"
if __name__ == "__main__":
    main()
