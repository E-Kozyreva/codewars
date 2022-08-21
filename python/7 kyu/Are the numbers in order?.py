# In this Kata, your function receives an array of integers as input. Your task is to determine whether the numbers are in ascending order. 
# An array is said to be in ascending order if there are no two adjacent integers where the left integer exceeds the right integer in value.

# For example:
# in_asc_order([1,2,4,7,19]) # returns True
# in_asc_order([1,2,3,4,5]) # returns True
# in_asc_order([1,6,10,18,2,4,20]) # returns False
# in_asc_order([9,8,7,6,5,4,3,2,1]) # returns False because the numbers are in DESCENDING order

def in_asc_order(arr):
    sort_arr = sorted(arr)
    flag = True
    for i in range(len(arr)):
        if arr[i] != sort_arr[i]:
            flag = False
    return flag
