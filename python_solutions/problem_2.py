def main():

    n = 4000000

    f1 = 1
    f2 = 1
    fn = f1 + f2
    total = 0

    while f2 <= n:
        if fn % 2 == 0:
            total += fn

        f1 = f2
        f2 = fn
        fn = f1 + f2

    return total

if __name__ == "__main__":
    print(main())
