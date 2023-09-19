from utils import euler_lib


def main():

    n = 20
    m = 20

    count = euler_lib.count_lattice_paths(n, m)

    return count


if __name__ == "__main__":
    print(main())
