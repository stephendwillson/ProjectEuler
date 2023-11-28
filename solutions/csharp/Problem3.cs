using System.Numerics;

namespace ProjectEuler
{
    class Problem3 : Problem
    {
        public override BigInteger Solve()
        {
            BigInteger n = 600851475143;

            List<BigInteger> primeFactors = EulerLib.GetPrimeFactors(n);

            return primeFactors.Max();
        }
    }
}