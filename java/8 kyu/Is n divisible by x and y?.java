// Create a function that checks if a number n is divisible by two numbers x AND y. All inputs are strictly positive numbers.

public class DivisibleNb {
	public static boolean isDivisible(long n, long x, long y) {
		if (n % x == 0 && n % y == 0){
      return true;
    } else {
      return false;
    }
	}
}
