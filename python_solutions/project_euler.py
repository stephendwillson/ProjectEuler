"""
Test harness for Project Euler problems
"""

import argparse
import subprocess
import os
import importlib
import pathlib

def main():

    problem_help = "Space-separated list of problems. Chooses ALL problems if none are specified."
    info_help = "Prints description of specified problems."
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--problem", help=problem_help, nargs="+")
    parser.add_argument("-i", "--info", help=info_help, action="store_true")

    args = parser.parse_args()

    problems = build_problem_list(args.problem)
    if args.info:
        print_problem_info(problems)
        exit()

def print_problem_info(problems):

    script_dir = os.path.dirname(os.path.abspath(__file__))

    for problem in problems:
        print("=" * 80)

        p_name = pathlib.Path(problem).stem
        print("Problem: {}".format(p_name))
        
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
