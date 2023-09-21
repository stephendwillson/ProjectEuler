import yaml

def load_problem_data(problem_number):

    with open("problem_data.yaml", "r") as config_file:
        config = yaml.safe_load(config_file)
        problems = config.get("problems", [])

        for problem in problems:
            if problem["number"] == problem_number:
                return problem

        return None