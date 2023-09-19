def main():

    palindromes = []

    for i in range(1, 1000):
        for j in range(1, 1000):
            prod = i * j

            if str(prod) == str(prod)[::-1]:
                palindromes.append(prod)

    return max(palindromes)


if __name__ == "__main__":
    print(main())
