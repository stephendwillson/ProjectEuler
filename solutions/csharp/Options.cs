using CommandLine;

namespace ProjectEuler
{
    class Options
    {
        [Option(
            'p', "problem",
            Required = false,
            Separator = ',',
            HelpText = "Space-separated list of problems. Chooses ALL problems if none are specified.")]
        public IEnumerable<int> ProblemNumbers { get; set; } = Enumerable.Empty<int>();

        [Option(
            'v', "verbose",
            Default = false,
            HelpText = "Prints description of specified problems.",
            Required = false)]
        public bool Verbose { get; set; }

        [Option(
            's', "solve",
            Default = false,
            HelpText = "Solve the specified problems. Does not solve by default.",
            Required = false)]
        public bool Solve { get; set; }

        [Option(
            't', "timer",
            Default = false,
            HelpText = "Display time taken to calculate solution in seconds.",
            Required = false)]
        public bool Timer { get; set; }

        [Option(
            "validate",
            Default = false,
            HelpText = "Throw ArgumentException if wrong solution is found.",
            Required = false)]
        public bool Validate { get; set; }
    }
}