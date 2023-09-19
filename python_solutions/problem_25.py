def main():

    n = 1000

    f1 = 1
    f2 = 1

    i = 2
    while len(str(f2)) < n:

        i += 1

        tmp = f2
        f2 = f1 + f2
        f1 = tmp

    return i


if __name__ == "__main__":
    print(main())
