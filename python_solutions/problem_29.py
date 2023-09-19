def main():

    floor = 2
    ceiling = 100

    # build a list of terms
    terms = []
    for i in range(floor, ceiling + 1):
        for j in range(floor, ceiling + 1):
            terms.append(i ** j)

    # remove dupes and sort
    terms = list(set(terms))
    terms.sort()

    return len(terms)


if __name__ == "__main__":
    print(main())
