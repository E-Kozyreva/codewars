// You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. 
// You need to count the number of 1s in the binary representations of all the numbers in the array.

function rangeBitCount(a, b) {
  var count = 0;
  for(let num = a; num <= b; num++)
    count += Number(num).toString(2).split("1").length - 1;
  return count;
}
