"""
Run Project Euler problem solver scripts
"""

import argparse
import importlib
import os
import pathlib
import time
import yaml


def parse_arguments():
    """
    Parse command-line args.

    :return: Parsed command-line args.
    :rtype: argparse.Namespace
    """

    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--problem",
                        help="Space-separated list of problems. Chooses ALL problems if none are specified.",
                        nargs="+")
    parser.add_argument("-v", "--verbose",
                        help="Prints description of specified problems.",
                        action="store_true")
    parser.add_argument("-s", "--solve",
                        help="Solve the specified problems. Does not solve by default.",
                        action="store_true")
    parser.add_argument("-t", "--timer",
                        help="Display time taken to calculate solution in seconds.",
                        action="store_true")
    parser.add_argument("--validate",
                        help="Raises ValueError if wrong solution is found.",
                        action="store_true")

    return parser.parse_args()


def load_config():
    """
    Load config info for problems from YAML.

    :return: Loaded config data.
    :rtype: dict
    """

    with open("problem_data.yaml", "r") as config_file:
        return yaml.safe_load(config_file)


def print_problem_info(problem, problem_data):
    """
    Print descriptive info about a specific problem.

    :param problem: The problem number.
    :type problem: int
    :param problem_data: Dict of problem data from YAML.
    :type problem_data: dict
    """

    print("=" * 79)

    found_problem = None

    for p in problem_data:
        if p["number"] == problem:
            found_problem = p
            break

    if not found_problem:
        print(f"Attempted to print problem info for nonexistent problem: {problem}")

    if found_problem:
        print(f"PROBLEM {found_problem['number']} - {found_problem['name']}")
        print(found_problem['url'])
        print()
        print(found_problem["description"])

    print("=" * 79)


def build_problem_list(problem_args, problem_data):
    """
    Build a list of problems to run.

    :param problem_args: List of problem numbers to run.
    :type problem_args: list of str
    :param problem_data: List of problem data dicts from YAML.
    :type problem_data: list of dict
    :return: List of problem data dicts for problems to run.
    :rtype: list of dict
    """

    # if no -p arg is passed, run every problem
    if not problem_args:
        return problem_data

    selected_problems = []

    for arg in problem_args:

        # don't forget to handle multiple specific problems
        problem_numbers = arg.split(',')
        for problem_num in problem_numbers:
            for problem in problem_data:
                if problem["number"] == problem_num.strip():
                    selected_problems.append(problem)

    # 'magic' sort before we hand it back
    return sorted(selected_problems, key=lambda x: int(x["number"]))


def solve_problem(problem, validate):
    """
    Solve the specified problem and optionally validate the solution.

    :param problem: Dict of problem data from YAML.
    :type problem: dict
    :param validate: If False, does not bother checking against the solution in YAML.
    :type validate: bool
    :raises ValueError: If the calculated solution does not match the solution in YAML.
    :return: The calculated solution.
    :rtype: int
    """

    # build path to problem script
    problem_script_filename = f"problem_{problem['number']}.py"
    problem_script_path = os.path.join("python_solutions", problem_script_filename)
    problem_path = pathlib.Path(problem_script_path)

    # just default to 0 if solution property doesn't exist in yaml
    expected_solution = int(problem.get("solution", 0))

    # import the solution script and run
    problem_script_name = f"problem_{problem['number']}"
    problem_script = importlib.import_module(f"python_solutions.{problem_script_name}")
    calculated_solution = problem_script.main()

    # validate the solution if specified
    if validate and expected_solution != calculated_solution:
        raise ValueError(
            "WRONG SOLUTION!\n"
            f"Expected {expected_solution}\n"
            f"Received {calculated_solution}"
        )

    return calculated_solution


def main():
    """
    Entry point for running Project Euler problem solver scripts.
    """

    args = parse_arguments()
    problem_data = load_config()
    problems = problem_data.get("problems", [])

    problem_list = build_problem_list(args.problem, problems)

    slowest = 0
    slowest_name = ""
    overall_time = 0
    problem_count = 0

    for problem in problem_list:
        if args.verbose:
            print_problem_info(problem["number"], problem_list)
        if args.solve:
            problem_count += 1

            start_time = time.process_time()
            solution = solve_problem(problem, args.validate)
            end_time = time.process_time()
            total_time = end_time - start_time
            overall_time += total_time

            problem_script_filename = f"problem_{problem['number']}.py"
            tidy_problem_name = pathlib.Path(problem_script_filename).stem.upper().replace("_", " ")

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


main()
