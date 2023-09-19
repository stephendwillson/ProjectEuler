import os

from utils import euler_lib


def main():

    supplemental_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
        "supplemental"
        )
    filepath = os.path.join(supplemental_dir, "p22_names.txt")
    with open(filepath, encoding='utf-8') as f:
        names_str = f.read()

    # clean up and sort list of names
    names = names_str.split(",")
    for i, _ in enumerate(names):
        names[i] = names[i].replace("\"", "")
    names.sort()

    total = 0
    for i, _ in enumerate(names):
        score = euler_lib.get_word_score(_)
        total += score * (i + 1)

    return total


if __name__ == "__main__":
    print(main())
