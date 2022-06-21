"""
https://projecteuler.net/problem=15

Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.

sdwillso NOTE: There's an image here in the original problem of all 6 routes to the bottom right corner.

How many such routes are there through a 20×20 grid?
"""

import euler_lib


n = 20
m = 20

count = euler_lib.count_lattice_paths(n, m)

print("total routes through {} x {} grid: {}".format(n, m, count))
