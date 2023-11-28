https://projecteuler.net/about#publish


Solutions and the scripts to obtain them for problems beyond 100 will not be posted per Project Euler publishing policy.
As the policy says, solving these problems can be pretty rewarding. I encourage giving it a shot coming up with your own solution.

# Project Euler
A collection of Project Euler solution scripts in various languages along with drivers to run them. The goals are entertainment and to refresh/maintain my programming skills. The goal is not to create every prime hunting, etc. algorithm from scratch.

# Usage
## Python
### `project_euler.py` Driver Script
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

#### Example Driver Usage
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

### Standalone
```
$ python python_solutions/problem_23.py 
1234567890
```

### `euler_lib.py` Common Library
Functions that are likely to show up repeatedly like hunting for prime numbers should live in `euler_lib.py`.

## C#
### Dependencies
CommandLineParser and YamlDotNet packages are required for the C# driver:
```bash
dotnet add package CommandLineParser --version 2.9.1
dotnet add package YamlDotNet --version 13.7.1
```

### Driver
The C# driver should function the same as the Python driver.
Solutions can be run using the driver, ProjectEuler. Running standalone
solutions is not currently supported.

**NOTE:** the driver does not solve by default. The -s | --solve argument must be passed.

```
Supported arguments:
  -p, --problem    Space-separated list of problems. Chooses ALL
                   problems if none are specified.

  -v, --verbose    (Default: false) Prints description of specified
                   problems.

  -s, --solve      (Default: false) Solve the specified problems. Does
                   not solve by default.

  -t, --timer      (Default: false) Display time taken to calculate
                   solution in seconds.

  --validate       (Default: false) Throw ArgumentException if wrong
                   solution is found.

  --help           Display this help screen.

  --version        Display version information.
```

#### Example Driver Usage
Navigate to `ProjectEuler/solutions/csharp`:
```
> dotnet build && dotnet run -- -s --validate -p 1
PROBLEM 1: 12345
```
```
> dotnet build && dotnet run -- -st --validate -p 2,1
PROBLEM 1: 233168
Time to solve: 0.000s

PROBLEM 2: 4613732
Time to solve: 0.000s

Time to solve all problems: 0.000s
```
```
> dotnet build && dotnet run -- -v -p 1
===============================================================================
PROBLEM 1 - MULTIPLES OF 3 OR 5
https://projecteuler.net/problem=1

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

===============================================================================
```

# Adding Solutions
- Information related to the problem such as the description, name, and URL should live in `problem_data.yaml`.
- The `solution` property in the YAML config file is meant to be manually set after solving the problem. It should be used as a sanity check when changes to a solution for efficiency, etc. are made. This means passing the `--validate` flag **should** cause an exception to be raised for solutions still under development.

## Python
- Each problem is expected to be in its own .py file
- Solution scripts are expected to be in the `solutions/python` directory.
- Solution scripts are expected to have a `main()` function that returns a single integer, the problem solution.

### Solution Template
```python
from utils import euler_lib


def main():

    return -1


if __name__ == "__main__":
    print(main())

```

## C#
- Solution files are expected to be in the `solutions/csharp` directory.
- Each solution is expected to contain a function `Solve()` that overrides the superclass Problem's `Solve()` function. `Solve()` is expected to return a single integer, the problem solution.
- Each problem is expected to be in its own file.
- Command line arguments are stored in `Options.cs`.
- All relevant files are expected to be in the same namespace, `ProjectEuler`.

### Solution Template
```csharp
namespace ProjectEuler
{
    class Problem1 : Problem
    {
        public override int Solve()
        {
            int total = 0;

            // do math-y things

            return total;
        }
    }
}
```

# Problem Config
# Supplemental Material
Any extra material required for a problem such as the list of names provided with Problem 22 should be placed in the `ProjectEuler/supplemental` directory.

For data related to the problem in `ProjectEuler/problem_data.yaml`:
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

# Tests
## Python
A set of Python tests are implemented using pytest.

### Organization
Tests should live in `project_root/tests/`.


`test_problems.py`
- Python solution script tests
- Runs `main()` functions of `problem_<n>.py` scripts and validates solutions
against solutions in `project_root/problem_data.yaml`

`test_euler_lib.py`
- Python utility library tests
- Executes every function prepended with `test_`

### Running Tests
Ensure pytest is installed:
```sh
pip install pytest
```

Navigate to project root and run:
```sh
pytest
```