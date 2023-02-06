import euler_lib


def main():

    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    coin_combos = euler_lib.num_coin_combos(coins, 200)

    return coin_combos

def description():

    desc = """
https://projecteuler.net/problem=31

In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:

    1x£1 + 1x50p + 2x20p + 1x5p + 1x2p + 3x1p

How many different ways can £2 be made using any number of coins?

"""
    print(desc, end="")

pe_name = "COIN SUMS"
pe_solution = 73682

if __name__ == "__main__":
    print(main())
