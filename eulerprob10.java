import java.util.*;

public class eulerprob10
{
	public static Scanner in = new Scanner(System.in);
	public static void main(String[] args)
	{
		long primesum=2L, test=1L, i=0L;
		boolean isPrime=false;

		while(test < 2000000-2)
		{
			test+=2;
			isPrime=true;
			for(i=3; i <= Math.sqrt(test); i+=2)
				if(test%i==0)
				{
					isPrime=false;
					break;
				}

			if(isPrime)
				primesum+=test;
		}
		System.out.println("Sum of primes below 2,000,000 is " + primesum);
		System.out.println("Program is finished. Acknowledge to close.");
		in.nextLine();
	}
}