namespace ProjectEuler
{
    class Problem2 : Problem
    {
        public override int Solve()
        {
            int n = 4000000;

            int f1 = 1;
            int f2 = 1;
            int fn = f1 + f2;
            int total = 0;

            while (f2 <= n)
            {
                if (fn % 2 == 0)
                {
                    total += fn;
                }
                f1 = f2;
                f2 = fn;
                fn = f1 + f2;
            }
            return total;
        }
    }
}