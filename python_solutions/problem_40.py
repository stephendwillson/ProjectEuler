def main():

    ceiling = 1000000

    # starting with a list and converting to string afterward runs
    # significantly faster than if we begin with a string
    d = []
    i = 0
    while len(d) < ceiling:
        i += 1
        d.append(str(i))

    d = ''.join(d)

    total = (
        int(d[0])
        * int(d[9])
        * int(d[99])
        * int(d[999])
        * int(d[9999])
        * int(d[99999])
        * int(d[999999])
    )

    return total


if __name__ == "__main__":
    print(main())
