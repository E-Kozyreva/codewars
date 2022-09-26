// For this first Kata, you will write a function hamming_distance(a, b) with two equal-length strings containing only 0s and 1s as parameters. 
// There is no need to test the parameters for validity (but you can, if you want).
// The function's output should be the hamming distance of the two strings as an integer.

function hammingDistance (a, b) {
  var count = 0;
  for (let i = 0; i < a.length; i++){
    if (a[i] != b[i])
      count++;
  }
  return count;
}
