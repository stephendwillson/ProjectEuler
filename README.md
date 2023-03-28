# Project Euler
Project Euler solutions and a driver to run them. The goal is to refresh and maintain Python skills.


# Usage
## `project_euler.py` Driver Script
Solutions can be run standalone or using the driver, project_euler.py.

**NOTE:** the driver does not solve by default. The -s | --solve argument must be passed.

```
Supported arguments:

-h, --help          Show this help message and exit.

-v, --verbose       Prints description of specified
                    problems.

-s, --solve         Solve the specified problems.
                    Does not solve by default.

-t, --timer         Display time taken to calculate solution  
                    in seconds.

--validate          Raises ValueError if wrong solution is    
                    found.

-p PROBLEM [PROBLEM ...], 
--problem PROBLEM [PROBLEM ...]       
                    Space-separated list of problems.
                    Chooses ALL problems if none are
                    specified.
```

## Example Driver Usage
```
$ python project_euler.py -p 13 -s
PROBLEM 13: 12345
```
```
$ python project_euler.py -p 10 11 -t -s
PROBLEM 10: 67890
Time to solve: 4.2656s

PROBLEM 11: 54321
Time to solve: 0.0000s


Number of problems solved: 2
Slowest problem to solve: PROBLEM 10
Time to solve PROBLEM 10: 4.27s
Time for all solutions: 4.27s
```
```
$ python project_euler.py -p 1 -v -t --validate -s
================================================================================
PROBLEM 1 - MULTIPLES OF 3 OR 5

https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.   

Find the sum of all the multiples of 3 or 5 below 1000.
================================================================================

PROBLEM 1: 98760
Time to solve: 0.0000s


Number of problems solved: 1
Slowest problem to solve:
Time to solve : 0.00s
Time for all solutions: 0.00s
```

## Standalone
```
$ python python_solutions/problem_23.py 
1234567890
```

# `euler_lib.py` Common Library
Functions that are likely to show up repeatedly like hunting for prime numbers should live in `euler_lib.py`.

**NOTE:** be sure to set the PYTHONPATH environment variable to allow scripts to find `euler_lib.py`:
```
export PYTHONPATH=/path/to/ProjectEuler/lib
```

# Supplemental Material
Any extra material required for a problem such as the list of names provided with Problem 22 should be placed in the `ProjectEuler/supplemental` directory.

# Adding Solutions
- Solution scripts are expected to be in the `python_solutions` directory.
- Solution scripts are expected to have a `main()` function that returns the problem solution.
- Solution scripts are expected to have several fields:
  - A description function, `def description()`
  - A problem name, `PE_NAME`
  - A solution, `PE_SOLUTION`
- The `PE_SOLUTION` variable is intended to be manually set only after the actual solution is found. It should be used as a sanity check when changes to a solution for efficiency, etc. are made. This means passing the `--validate` flag **should** cause a `ValueError` to be raised for solutions still under development.
- A directive should be added to allow running standalone in addition to driver-initiated:
```python
if __name__ == "__main__":
    print(main())
```

## Solution Template
A basic template for implementing new solution scripts:
```python
import euler_lib


def main():

    return -1


def description():

    desc = """
https://projecteuler.net/problem=N

The descriptive text of the problem from the Project Euler site goes here.
"""
    print(desc, end="")

PE_NAME = "PROBLEM NAME"
PE_SOLUTION = 0

if __name__ == "__main__":
    print(main())
```
