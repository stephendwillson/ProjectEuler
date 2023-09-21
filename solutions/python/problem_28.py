from utils import euler_lib


def main():

    # grid dimensions
    n = 1001
    m = 1001

    # maximum value of the spiral
    ceiling = n * m

    # make the spiral
    spiral = euler_lib.generate_number_spiral(ceiling)

    # voila
    d_sum = euler_lib.get_matrix_diagonals_sum(spiral)

    return d_sum


if __name__ == "__main__":
    print(main())
