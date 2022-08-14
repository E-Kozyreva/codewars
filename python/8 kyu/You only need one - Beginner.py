# You will be given an array a and a value x. All you need to do is check whether the provided array contains the value.
# Array can contain numbers or strings. X can be either.
# Return true if the array contains the value, false if not.

def check(seq, elem):
    flag = False
    
    for num in seq:
        if num == elem:
            flag = True
            
    return flag
