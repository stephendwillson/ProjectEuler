import os

from utils import euler_lib


def main():

    # arbitrary upper bound == word 'ZZZZZZZZZZ' = 26*10 = 260
    # grab a close triangle number, 23 == 276
    n = 23

    triangles = []
    for i in range(1, n + 1):
        triangles.append(euler_lib.get_triangle_number(i))

    # read in words
    supplemental_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
        "supplemental")
    filepath = os.path.join(supplemental_dir, "p42_words.txt")
    with open(filepath, encoding='utf-8') as f:
        words_str = f.read()

    # clean up
    words = words_str.split(",")
    for word in words:
        word = word.replace("\"", "")

    total = 0
    for word in words:
        score = euler_lib.get_word_score(word)
        if score in triangles:
            total += 1

    return total


if __name__ == "__main__":
    print(main())
