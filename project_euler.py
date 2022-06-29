"""
Run Project Euler problem solver scripts
"""

import time
import argparse
import subprocess
import os
import sys
import importlib
import pathlib

def main():

    problem_help = "Space-separated list of problems. Chooses ALL problems if none are specified."
    verbose_help = "Prints description of specified problems."
    solve_help = "Solve the specified problems. Does not solve by default."
    timer_help = "Display time taken to calculate solution in seconds."
    validate_help = "Raises ValueError if wrong solution is found."

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem", help=problem_help, nargs="+")
    parser.add_argument("-v", "--verbose", help=verbose_help, action="store_true")
    parser.add_argument("-s", "--solve", help=solve_help, action="store_true")
    parser.add_argument("-t", "--timer", help=timer_help, action="store_true")
    parser.add_argument("--validate", help=validate_help, action="store_true")

    args = parser.parse_args()

    problems = build_problem_list(args.problem)
    
    for problem in problems:
        if args.verbose:
            print_problem_info(problem)
        if args.solve:
            start_time = time.process_time()
            solution = solve_problem(problem, args.validate)
            end_time = time.process_time()

            print("{}: {}".format(pathlib.Path(problem).stem.upper().replace("_", " "), solution))
            if args.timer:
                print("Time to solve: {0:.4f}s".format(end_time - start_time))

def solve_problem(problem, validate):

    p_name = pathlib.Path(problem).stem
    p = importlib.import_module(p_name)

    solution = p.main()

    if validate:
        if solution != p.pe_solution:
            raise ValueError("WRONG SOLUTION! Expected {} Received {}".format(p.pe_solution, solution))

    return solution

def print_problem_info(problem):

    print("=" * 80)

    p_name = pathlib.Path(problem).stem 
    p = importlib.import_module(p_name)

    print("{} - {}".format(p_name.upper().replace("_", " "), p.pe_name))
    p.description()

    print("=" * 80)
    print()


def build_problem_list(problem_args):

    p_list = []
    script_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "python_solutions")

    # clunky -- this is so imports in solving and printing info work with this script in separate dir
    sys.path.append(script_dir)

    # if no -p arg is passed in, run all problems
    if problem_args is None:
        for root, dirs, files in os.walk(script_dir):
            for file in files:
                if file.startswith("problem") and file.endswith(".py"):
                    path = "{}/{}".format(script_dir, file)
                    p_list.append(path)

    else:
        for p in problem_args:
            
            path = "{}/problem_{}.py".format(script_dir, p)
            if os.path.exists(path):
                p_list.append(path)

    # "magic" - sort file names by problem number
    p_list.sort(key=lambda f: int("".join(filter(str.isdigit, f))))
    
    return p_list

main()
