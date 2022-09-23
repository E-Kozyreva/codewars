# Given an array of integers, remove the smallest value. Do not mutate the original array/list. 
# If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

def remove_smallest(numbers):
    if len(numbers) == 0:
        return numbers
    else:
        index_n = numbers.index(min(numbers))
        return [numbers[i] for i in range(len(numbers)) if i != index_n]
