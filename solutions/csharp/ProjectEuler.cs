using System.Diagnostics;
using System.Reflection;

using YamlDotNet.Core;
using YamlDotNet.Serialization;
using YamlDotNet.Serialization.NamingConventions;
using CommandLine;


namespace ProjectEuler
{
    class ProjectEuler
    {
        static void Main(string[] args)
        {
            IEnumerable<int> problemNumbersArg = Enumerable.Empty<int>();
            bool verbose = false;
            bool solve = false;
            bool timer = false;
            bool validate = false;

            // read in all the cli args
            var parsedOptions = CommandLine.Parser.Default.ParseArguments<Options>(args);
            parsedOptions.WithParsed(options =>
            {
                problemNumbersArg = options.ProblemNumbers;
                verbose = options.Verbose;
                solve = options.Solve;
                timer = options.Timer;
                validate = options.Validate;
            });

            // load in problem data from the problem data yaml
            YamlProblemList yamlProblemList = LoadConfig("../../problem_data.yaml", problemNumbersArg);

            // as long as we find some problems defined in yaml...
            if (yamlProblemList.Problems != null)
            {
                // check that every specified -p exists in the problem data yaml
                var invalidProblemNumbers = problemNumbersArg.Except(yamlProblemList.Problems.Select(p => p.Number));
                if (invalidProblemNumbers.Any())
                {
                    throw new ArgumentException(
                        $"Problem(s) not found in YAML problem data file: {string.Join(", ", invalidProblemNumbers)}");
                }

                // cycle through every problem and do the things
                double totalTime = 0;
                foreach (var yamlProblem in yamlProblemList.Problems)
                {
                    // get an instance of Problem<n> class from Problem<n>.cs
                    Problem problem = Problem.GetProblemClass(yamlProblem);
                    if (verbose)
                    {
                        problem.PrintProperties();
                    }

                    // let's solve
                    if (solve)
                    {
                        var stopwatch = Stopwatch.StartNew();
                        int solution = problem.Solve();
                        stopwatch.Stop();
                        totalTime += stopwatch.Elapsed.TotalSeconds;

                        Console.WriteLine($"PROBLEM {problem.Number}: {solution}");

                        if (timer)
                        {
                            Console.WriteLine($"Time to solve: {stopwatch.Elapsed.TotalSeconds:F3}s\n");
                        }

                        //check our solution against the solution in the problem data yaml
                        if (validate)
                        {
                            if (solution != problem.Solution)
                            {
                                throw new ArgumentException(
                                    $"WRONG SOLUTION!\n" +
                                    $"Expected {problem.Solution}\n" +
                                    $"Received {solution}");
                            }
                        }
                    }
                }

                if (timer)
                {
                    Console.WriteLine($"Time to solve all problems: {totalTime:F3}s");
                }
            }
        }

        // grab a list of every relevant Problem with an entry in problem data yaml
        static YamlProblemList LoadConfig(string yamlPath, IEnumerable<int> problemNumbers)
        {
            YamlProblemList problemList = new();

            try
            {
                var deserializer = new DeserializerBuilder()
                    .WithNamingConvention(CamelCaseNamingConvention.Instance)
                    .Build();
                var yamlText = File.ReadAllText(yamlPath);

                // automagically sets Problem object's fields from yaml attributes
                problemList = deserializer.Deserialize<YamlProblemList>(yamlText);

                // we only want to return config for specified problems, filter out the rest
                if (problemNumbers.Any())
                {
                    problemList.Problems = problemList.Problems?.Where(p => problemNumbers.Contains(p.Number)).ToList();
                }
                // if no problems are specified, return config for every problem that has an associated class/.cs file
                else
                {
                    /*
                     * get classes/interfaces/etc. in this assembly...
                     * ...filter down to just classes in namespace ProjectEuler named "Problem(...)"...
                     * ...and strip the number out of the class name Problem<n> and assign number = <n>
                     */
                    var problemClassNumbers = Assembly.GetExecutingAssembly()
                        .GetTypes()
                        .Where(t => t.IsClass && t.Namespace == "ProjectEuler" && t.Name.StartsWith("Problem"))
                        .Select(t => int.TryParse(t.Name.Replace("Problem", ""), out var number) ? number : (int?)null);

                    // remove problems from the list that don't have a Problem<n> class
                    problemList.Problems = problemList.Problems?.Where(p => problemClassNumbers.Contains(p.Number)).ToList();
                }
            }
            catch (YamlException ex)
            {
                Console.WriteLine($"YamlException loading YAML: {ex.Message}");
                Console.WriteLine($"At {yamlPath} line {ex.Start.Line}, column {ex.Start.Column}");
            }
            catch (Exception ex)
            {
                Console.WriteLine($"Generic exception loading YAML: {ex.Message}");
            }

            return problemList;
        }
    }
}
