"""
Test harness for Project Euler problems
"""

import time
import argparse
import subprocess
import os
import importlib
import pathlib

def main():

    problem_help = "Space-separated list of problems. Chooses ALL problems if none are specified."
    verbose_help = "Prints description of specified problems."
    solve_help = "Solve the specified problems. Does not solve by default."

    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem", help=problem_help, nargs="+")
    parser.add_argument("-v", "--verbose", help=verbose_help, action="store_true")
    parser.add_argument("-s", "--solve", help=solve_help, action="store_true")

    args = parser.parse_args()

    problems = build_problem_list(args.problem)
    
    for problem in problems:
        if args.verbose:
            print_problem_info(problem)
        if args.solve:
            solution = solve_problem(problem)
            clean_name = pathlib.Path(problem).stem.upper().replace("_", " ")
            print("{}: {}".format(clean_name, solution))

def solve_problem(problem):

    solution = 0
    # solve solve solve

    return solution

def print_problem_info(problem):

    script_dir = os.path.dirname(os.path.abspath(__file__))

    print("=" * 80)

    p_name = pathlib.Path(problem).stem
    print("{}".format(p_name.upper().replace("_", " ")))
    
    p = importlib.import_module(p_name)
    p.description()

    print("=" * 80)
    print()


def build_problem_list(problem_args):

    p_list = []
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # if no -p arg is passed in, run all problems
    if problem_args is None:
        for root, dirs, files in os.walk(script_dir):
            for file in files:
                if file.startswith("problem") and file.endswith(".py"):
                    path = "{}/{}".format(script_dir, file)
                    p_list.append(path)
        
        return p_list

    else:
        for p in problem_args:
            
            path = "{}/problem_{}.py".format(script_dir, p)
            if os.path.exists(path):
                p_list.append(path)

        return p_list

main()
