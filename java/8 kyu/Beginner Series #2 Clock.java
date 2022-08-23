// Clock shows h hours, m minutes and s seconds after midnight.
// Your task is to write a function which returns the time since midnight in milliseconds.

// Example:
// h = 0
// m = 1
// s = 1
// result = 61000

public class Clock
{
  public static int Past(int h, int m, int s) 
  {
    int resultHours = h * 3600000;
    int resultMinutes = m * 60000;
    int resultSeconds = s * 1000;
    return resultHours + resultMinutes + resultSeconds;
  }
}
