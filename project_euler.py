"""
Run Project Euler problem solver scripts
"""

import time
import argparse
import os
import sys
import importlib
import pathlib


# pylint: disable=too-many-locals
def main():

    problem_help_text = \
        "Space-separated list of problems. " \
        "Chooses ALL problems if none are specified."
    solve_help_text = \
        "Solve the specified problems. " \
        "Does not solve by default."
    verbose_help_text = "Prints description of specified problems."
    timer_help_text = "Display time taken to calculate solution in seconds."
    validate_help_text = "Raises ValueError if wrong solution is found."

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem",
                        help=problem_help_text, nargs="+")
    parser.add_argument("-v", "--verbose",
                        help=verbose_help_text, action="store_true")
    parser.add_argument("-s", "--solve",
                        help=solve_help_text, action="store_true")
    parser.add_argument("-t", "--timer",
                        help=timer_help_text, action="store_true")
    parser.add_argument("--validate",
                        help=validate_help_text, action="store_true")

    args = parser.parse_args()

    problems = build_problem_list(args.problem)

    slowest = 0
    slowest_name = ""

    overall_time = 0

    problem_count = 0

    for problem in problems:
        if args.verbose:
            print_problem_info(problem)
        if args.solve:
            problem_count += 1

            start_time = time.process_time()
            solution = solve_problem(problem, args.validate)
            end_time = time.process_time()
            total_time = end_time - start_time
            overall_time += total_time

            tidy_problem_name = \
                pathlib.Path(problem).stem.upper().replace("_", " ")

            if total_time > slowest:
                slowest = total_time
                slowest_name = tidy_problem_name

            print(f"{tidy_problem_name}: {solution}")

            if args.timer:
                print(f"Time to solve: {end_time - start_time:.4f}s")
                print()

    if args.timer:
        print()
        print(f"Number of problems solved: {problem_count}")
        print(f"Slowest problem to solve: {slowest_name}")
        print(f"Time to solve {slowest_name}: {slowest:.2f}s")
        print(f"Time for all solutions: {overall_time:.2f}s")

# pylint: enable=too-many-locals


def solve_problem(problem, validate):
    """
    Solve the specified problem. Validate solution if specified.

    :param problem: Problem number
    :type problem: int
    :param validate: Check whether solution is correct
    :type validate: bool
    :raises ValueError: ValueError is solution is incorrect
    :rtype: int
    """

    problem_name = pathlib.Path(problem).stem
    problem_script = importlib.import_module(problem_name)

    solution = problem_script.main()

    if validate:
        if solution != problem_script.PE_SOLUTION:
            raise ValueError(
                "WRONG SOLUTION!\n"
                f"Expected {problem_script.PE_SOLUTION}\n"
                f"Received {solution}"
                )

    return solution


def print_problem_info(problem):
    """
    Print the problem summary as seen on the Project Euler problem page.

    :param problem: Problem number
    :type problem: int
    """

    print("=" * 79)

    problem_name = pathlib.Path(problem).stem
    problem_script = importlib.import_module(problem_name)

    print(
        f"{problem_name.upper().replace('_', ' ')} - {problem_script.PE_NAME}")
    problem_script.description()

    print("=" * 79)
    print()


def build_problem_list(problem_args):
    """
    Build a list of paths of problem scripts to run.

    :param problem_args: -p command line params
    :type problem_args: list
    :return: List of paths of problem scripts to run
    :rtype: int list
    """

    p_list = []
    script_dir = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "python_solutions")

    # clunky -- this is so imports in solving and printing info work with
    # this script living in separate dir
    sys.path.append(script_dir)

    # if no -p arg is passed in, run all problems
    if problem_args is None:
        for _, _, files in os.walk(script_dir):  # root, dir, files
            for file in files:
                if file.startswith("problem") and file.endswith(".py"):
                    path = f"{script_dir}/{file}"
                    p_list.append(path)

    else:
        for problem_num in problem_args:

            path = f"{script_dir}/problem_{problem_num}.py"
            if os.path.exists(path):
                p_list.append(path)

    # "magic" - sort file names by problem number
    p_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))

    return p_list


main()
