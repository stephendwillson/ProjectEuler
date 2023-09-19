import math

nums = {
    "0": "zero",
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four",
    "5": "five",
    "6": "six",
    "7": "seven",
    "8": "eight",
    "9": "nine",
    "10": "ten",
    "11": "eleven",
    "12": "twelve",
    "13": "thirteen",
    "14": "fourteen",
    "15": "fifteen",
    "16": "sixteen",
    "17": "seventeen",
    "18": "eighteen",
    "19": "nineteen",
    "20": "twenty",
    "30": "thirty",
    "40": "forty",
    "50": "fifty",
    "60": "sixty",
    "70": "seventy",
    "80": "eighty",
    "90": "ninety"
}


def main():

    n = 1000
    word = ""

    for i in range(1, n + 1):
        word += parse(str(i))

    return len(word)


def parse(n):

    # 0-9
    if len(n) == 1:
        return nums[n]

    # 10-99
    if len(n) == 2:
        return get_tens(n)

    # 100-999
    if len(n) == 3:
        return get_hundreds(n)

    # 1000
    return f"{nums[n[0]]}thousand"


def get_tens(n):

    # 00, 01, ... , 08, 09
    if n[0] == "0":
        n = n[1:]

    # 1-19
    if int(n) < 20:
        return nums[n]

    # 20, 30, ... , 80, 90
    if int(n) % 10 == 0:
        return nums[n]

    # x != 0: 2x, 3x, ... , 8x, 9x
    tens = str(math.floor(int(n) / 10) * 10)

    tens = nums[tens]
    ones = nums[n[-1]]

    return f"{tens}{ones}"


def get_hundreds(n):

    # 1000
    if int(n) == "000":
        return ""

    # 100, 200, ... , 800, 900
    if int(n) % 100 == 0:
        return f"{nums[n[0]]}hundred"

    # 101, 102, ... 989, 999
    tens = get_tens(n[-2:])

    return f"{nums[n[0]]}hundredand{tens}"


if __name__ == "__main__":
    print(main())
