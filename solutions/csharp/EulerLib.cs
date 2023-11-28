using System.Numerics;

namespace ProjectEuler
{
    class EulerLib
    {
        /// <summary>
        /// Find all the prime factors of a number using trial division.
        /// </summary>
        /// <param name="n">The BigInteger for which to find prime factors.</param>
        /// <returns>A list of prime factors of the input BigInteger.</returns>
        public static List<BigInteger> GetPrimeFactors(BigInteger n)
        {
            if (n < 2)
            {
                return new List<BigInteger>();
            }

            List<BigInteger> primeFactors = new();

            // check 2 as a factor
            while (n % 2 == 0)
            {
                primeFactors.Add(2);
                n /= 2;
            }

            // check odd factors up to sqrt(n)
            for (int c = 3; c <= Math.Sqrt((double)n); c += 2)
            {
                while (n % c == 0)
                {
                    primeFactors.Add(c);
                    n /= c;
                }
            }

            // if n is still greater than 2, it must be prime
            if (n > 2)
            {
                primeFactors.Add(n);
            }

            return primeFactors;
        }

        /// <summary>
        /// Checks if a given number is a palindrome.
        /// </summary>
        /// <param name="number">The number to check for palindromicity.</param>
        /// <returns>True if the number is a palindrome, false otherwise.</returns>
        public static bool IsPalindrome(int number)
        {
            IEnumerable<char> forwards = number.ToString().ToCharArray();

            return forwards.SequenceEqual(forwards.Reverse());
        }
    }
}