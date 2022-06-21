"""
https://projecteuler.net/problem=22

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import string

def main():

    filepath = "../supplemental/p22_names.txt"
    with open(filepath) as f:
        names_str = f.read()

    # clean up and sort list of names
    names = names_str.split(",")
    for i in range(len(names)):
        names[i] = names[i].replace("\"", "")
    names.sort()

    # search for every char in A-Z and add position in alphabet to total
    total = 0
    i = 0
    for name in names:

        i += 1
        name_score = 0

        tmp = 0
        for char in name:
            char_index = string.ascii_uppercase.find(char)
            if char_index != -1:
                tmp += char_index + 1 # A == [0] --> A == 1 score

        name_score = tmp * i
        total += name_score

    print("total name score: {}".format(total))

main()
