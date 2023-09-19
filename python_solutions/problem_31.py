from utils import euler_lib


def main():

    coins = [1, 2, 5, 10, 20, 50, 100, 200]

    coin_combos = euler_lib.num_coin_combos(coins, 200)

    return coin_combos


if __name__ == "__main__":
    print(main())
