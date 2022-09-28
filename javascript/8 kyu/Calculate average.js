// Write a function which calculates the average of the numbers in a given list.
// Note: Empty arrays should return 0.

function findAverage(array) {
  if (Object.keys(array).length > 0) {
    const sum = array.reduce((partialSum, a) => partialSum + a, 0);
    return sum / Object.keys(array).length;
  } else {
    return 0;
  }
}
