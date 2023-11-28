using System.Numerics;

namespace ProjectEuler
{
    class Problem4 : Problem
    {
        public override BigInteger Solve()
        {
            int ceiling = 1000;
            List<int> palindromes = new();

            for (int i = 1; i < ceiling; i++)
            {
                for (int j = 1; j < ceiling; j++)
                {
                    int prod = i * j;

                    if (EulerLib.IsPalindrome(prod))
                    {
                        palindromes.Add(prod);
                    }
                }
            }

            return palindromes.Max();
        }
    }
}