def main():

    n = 1000

    total = 0
    for i in range(1, n + 1):
        total += i**i

    return int(str(total)[-10:])


if __name__ == "__main__":
    print(main())
