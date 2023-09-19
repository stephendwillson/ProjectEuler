import os

from utils import euler_lib


def main():

    t = []

    supplemental_dir = os.path.join(
        os.path.dirname(os.path.dirname(os.path.realpath(__file__))),
        "supplemental")

    filepath = os.path.join(supplemental_dir, "p67_triangle.txt")

    with open(filepath, encoding='utf-8') as f:
        t_lines = f.readlines()
        for line in t_lines:
            t.append(line.split())

    # convert everything to ints for euler_lib max path math
    t = get_int_grid(t)

    return euler_lib.get_triangle_max_path_sum(t)


def get_int_grid(t):

    tmp = []
    for line in t:
        tmp.append(list(map(int, line)))

    return tmp


if __name__ == "__main__":
    print(main())
