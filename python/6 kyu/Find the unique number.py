# There is an array with some numbers. All numbers are equal except for one. Try to find it!
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.

# The tests contain some very huge arrays, so think about performance.
# This is the first kata in series:
# Find the unique number (this kata)
# Find the unique string
# Find The Unique

def find_uniq(arr):
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            if i == 0 and arr[i] != arr[i + 2]:
                return arr[i]
            return arr[i + 1]
