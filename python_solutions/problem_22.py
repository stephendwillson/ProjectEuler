import os

import euler_lib


def main():

    supplemental_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "supplemental")
    filepath = os.path.join(supplemental_dir, "p22_names.txt")
    with open(filepath) as f:
        names_str = f.read()

    # clean up and sort list of names
    names = names_str.split(",")
    for i in range(len(names)):
        names[i] = names[i].replace("\"", "")
    names.sort()

    total = 0
    for i in range(len(names)):
        score = euler_lib.get_word_score(names[i])
        total += score * (i + 1)

    return total

def description():

    desc = """
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?
"""
    print(desc, end="")

pe_name = "NAMES SCORES"
pe_solution = 871198282

if __name__ == "__main__":
    print(main())
