https://projecteuler.net/about#publish


Solutions and the scripts to obtain them for problems beyond 100 will not be posted per Project Euler publishing policy.
As the policy says, solving these problems can be pretty rewarding. I encourage giving it a shot coming up with your own solution.


# Project Euler
A collection of Project Euler solution scripts and a driver to run them. The goal is to refresh and maintain my Python skills.
The goal is not to create every prime hunting, etc. algorithm from scratch.


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
                    Comma- or space-separated list of problems.
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

PROBLEM 1: 1234567890
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

# Supplemental Material
Any extra material required for a problem such as the list of names provided with Problem 22 should be placed in the `ProjectEuler/supplemental` directory.

# Adding Solutions
- Solution scripts are expected to be in the `python_solutions` directory.
- Solution scripts are expected to have a `main()` function that returns the problem solution.
- Information related to the problem such as the description, name, and URL should live in `problem_data.yaml`.
- The `solution` property in the YAML config file is meant to be manually set after solving the problem. It should be used as a sanity check when changes to a solution for efficiency, etc. are made. This means passing the `--validate` flag **should** cause a `ValueError` to be raised for solutions still under development.

## Solution Template
A basic template for implementing new solution scripts:
```python
from utils import euler_lib


def main():

    return -1


if __name__ == "__main__":
    print(main())

```

For data related to the problem:
```yaml
problems:
  - number: "1"
    name: "MULTIPLES OF 3 OR 5"
    url: "https://projecteuler.net/problem=1"
    description: |
      If we list all the natural numbers below 10 that are multiples of 3 or 5,
      we get 3, 5, 6, and 9. The sum of these multiples is 23.
      
      Find the sum of all the multiples of 3 or 5 below 1000.
    solution: 12345
```
