namespace ProjectEuler
{
    class Problem
    {
        public int Number { get; set; } = -1;
        public string Name { get; set; } = string.Empty;
        public string Url { get; set; } = string.Empty;
        public string Description { get; set; } = string.Empty;
        public long Solution { get; set; } = -1;

        public virtual int Solve()
        {
            return -1;
        }

        public void PrintProperties()
        {
            Console.WriteLine(new string('=', 79));
            Console.WriteLine($"PROBLEM {Number} - {Name}");
            Console.WriteLine(Url);
            Console.WriteLine();
            Console.WriteLine(Description);
            Console.WriteLine(new string('=', 79));
        }

        // find and return the Problem<N> class for the provided Problem
        public static Problem GetProblemClass(Problem yamlProblem)
        {
            Type? problemClass = Type.GetType($"ProjectEuler.Problem{yamlProblem.Number}");

            if (problemClass != null)
            {
                if (Activator.CreateInstance(problemClass) is Problem problemInstance)
                {
                    problemInstance.Number = yamlProblem.Number;
                    problemInstance.Name = yamlProblem.Name;
                    problemInstance.Url = yamlProblem.Url;
                    problemInstance.Description = yamlProblem.Description;
                    problemInstance.Solution = yamlProblem.Solution;

                    return problemInstance;
                }
                else
                {
                    throw new InvalidOperationException("Exception creating problem instance.");
                }
            }
            else
            {
                throw new InvalidOperationException($"Problem {yamlProblem.Number} class not found.");
            }
        }
    }
}