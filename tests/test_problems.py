import os
import importlib
import pytest

from tests.test_utils import load_problem_data
import solutions
import solutions.python


# discover every problem script
problem_module_dir = os.path.dirname(solutions.python.__file__)
problem_modules = [
    filename.split("_")[1][:-3]  # isolate problem # and remove .py extension
    for filename in os.listdir(problem_module_dir)
    if filename.startswith("problem_") and filename.endswith(".py")
]

@pytest.mark.parametrize("problem_number", problem_modules)
def test_problem_solution(problem_number):

    # import and run the problem solver script
    module_name = f"solutions.python.problem_{problem_number}"
    problem_script = importlib.import_module(module_name)

    calculated_solution = problem_script.main()

    # check our work
    problem_data = load_problem_data(problem_number)
    expected_solution = int(problem_data["solution"])

    assert calculated_solution == expected_solution