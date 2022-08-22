# Give your answer as a string matching "odd" or "even".
# If the input array is empty consider it as: [0] (array with a zero).

# Examples:
# Input: [0]
# Output: "even"

# Input: [0, 1, 4]
# Output: "odd"

def odd_or_even(arr):
    sumNumbers = sum(arr)
    if sumNumbers % 2 == 0:
        return "even"
    else:
        return "odd"
