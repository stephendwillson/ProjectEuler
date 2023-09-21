def main():

    ceiling = 1000000

    # create cache
    lengths_cache = [-1] * ceiling
    lengths_cache[1] = 1

    max_length = 0
    max_length_n = 0
    for i in range(2, ceiling):
        n = i
        seq_length = 0

        while n > 1:

            # if we get cache hit, add number to current length and bail out
            if n < i and lengths_cache[n] != -1:
                seq_length += lengths_cache[n]
                break

            # collatz
            if n % 2 == 0:
                n = n // 2
            else:
                n = 3*n + 1

            seq_length += 1

        # update cache
        lengths_cache[i] = seq_length

        if seq_length > max_length:
            max_length = seq_length
            max_length_n = i

    return max_length_n


if __name__ == "__main__":
    print(main())
