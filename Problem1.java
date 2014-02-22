/*
 	If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

	Find the sum of all the multiples of 3 or 5 below 1000.
 */

public class Problem1 {
	
	public static void main(String[] args) {
		
		//sum of all multiples less than 10 given in problem, no reason to not use that info
		int sum = 23;
		int ceiling = 1000;
		
		for (int i=10; i < ceiling; i++) {
			if (i%3==0 || i%5==0)
				sum += i;
		}
		
		System.out.println("Sum of all multiples of 3 or 5 below " + ceiling + " is " + sum + ".");
	}
}