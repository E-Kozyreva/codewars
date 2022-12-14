# Given an array of ones and zeroes, convert the equivalent binary value to an integer.
# Eg: [0, 0, 0, 1] is treated as 0001 which is the binary representation of 1.

# Examples:
# Testing: [0, 0, 0, 1] ==> 1
# Testing: [0, 0, 1, 0] ==> 2
# Testing: [0, 1, 0, 1] ==> 5

# However, the arrays can have varying lengths, not just limited to 4.

def binary_array_to_number(arr):
    number = 0
    for n in range(len(arr)):
        number += (2 ** n) * arr[::-1][n]
    return number
