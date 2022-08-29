# Define a method/function that removes from a given array of integers all the values contained in a second array.
# Examples (input -> output):
# [1, 1, 2 ,3 ,1 ,2 ,3 ,4], [1, 3] -> [2, 2, 4]

class List:
    def remove_(self, integer_list, values_list):
        return [num for num in integer_list if num not in values_list]
