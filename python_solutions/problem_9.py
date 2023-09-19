import math


def main():

    triplet = get_triplet()

    # convert list to int for math.prod
    triplet = [int(i) for i in triplet]

    return math.prod(triplet)


def get_triplet():
    """
    Square sum relation: (a^2 + b^2 = c^2) == (c^2 = m^4 + n^4 + 2*m^2*n^2)
    """

    c = 0
    m = 0

    while True:
        for n in range(1, m):
            a = m*m - n*n
            b = 2*m*n
            c = m*m + n*n

            if a + b + c == 1000:
                return [a, b, c]

        m += 1

    return None


if __name__ == "__main__":
    print(main())
