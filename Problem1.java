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