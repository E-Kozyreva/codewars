// Complete the function which takes two arguments and returns all numbers which are divisible by the given divisor. 
// First argument is an array of numbers and the second is the divisor.

// Example(Input1, Input2 --> Output)
// [1, 2, 3, 4, 5, 6], 2 --> [2, 4, 6]


public class EvenNumbers {
  public static int[] divisibleBy(int[] numbers, int divider) {
    int countNumbers = 0;
    for (int number : numbers){
      if (number % divider == 0)
        countNumbers++;
    }
    int[] newNumbers = new int[countNumbers];
    int numberIndex = 0;  
    for (int number : numbers){
      if (number % divider == 0){
        newNumbers[numberIndex] = number;
        numberIndex++;
      }        
    }
    return newNumbers;
  }
}
