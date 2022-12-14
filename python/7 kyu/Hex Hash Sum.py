# Complete the function that accepts a valid string and returns an integer.
# Wait, that would be too easy! Every character of the string should be converted to the hex value of its ascii code, 
# then the result should be the sum of the numbers in the hex strings (ignore letters).

def hex_hash(code):
    string = code.encode("utf-8").hex()
    sum_numbers = 0
    for symb in string:
        if symb in "0123456789":
            sum_numbers += int(symb)
    return sum_numbers
