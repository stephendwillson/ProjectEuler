import euler_lib


def main():

    # arbitrary upper bound == word 'ZZZZZZZZZZ' = 26*10 = 260
    # grab a close triangle number, 23 == 276
    n = 23

    triangles = list()
    for i in range(1, n + 1):
        triangles.append(euler_lib.get_triangle_number(i))

    # read in words
    filepath = "../supplemental/p42_words.txt"
    with open(filepath) as f:
        words_str = f.read()

    # clean up
    words = words_str.split(",")
    for i in range(len(words)):
        words[i] = words[i].replace("\"", "")

    total = 0
    for word in words:
        
        score = euler_lib.get_word_score(word)
        if score in triangles:
            total += 1

    return total

def description():

    desc = """
https://projecteuler.net/problem=42

The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing nearly two-thousand common English words, how many are triangle words?
"""
    print(desc, end="")
pe_name = "CODED TRIANGLE NUMBERS"
if __name__ == "__main__":
    main()
