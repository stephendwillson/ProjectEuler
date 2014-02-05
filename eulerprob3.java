import java.util.*;
import java.io.*;

public class eulerprob3
{
	public static Scanner in = new Scanner(System.in);

	public static void main(String[] args)
	{
		long target = 600851475143L;
		long test=0L;
		long i=1L;
		long largestprimefactor=0L;
		boolean isPrime=false;


		while(i < Math.sqrt(target))
		{
			i+=2L;
			if(target%i==0)
			{
				test=i;
				isPrime=true;
				for(long j=3L; j < Math.sqrt(i); j+=2L)
				{
					if(test%j==0)
					{
						isPrime=false;
						break;
					}
				}

				if(isPrime && test >= largestprimefactor)
				{
					largestprimefactor = test;
				}

			}
		}
		System.out.println("The largest prime factor of " + target + " is " + largestprimefactor + ".");
	}
}

//test if is factor
//test if it is prime
//test if larger than current largest
//rinse, repeat