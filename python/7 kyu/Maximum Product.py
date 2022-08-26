# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
# Array/list size is at least 2.
# Array/list numbers could be a mixture of positives, negatives also zeroes .

# adjacentElementsProduct([1, 2, 3]); ==> return 6
# The maximum product obtained from multiplying 2 * 3 = 6, and they're adjacent numbers in the array.

def adjacent_element_product(array):
    return max([array[i - 1] * array[i] for i in range(1, len(array))])
