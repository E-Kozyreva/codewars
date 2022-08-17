# Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(string):
    min_len = 100
    words = string.split()
    
    for s in words:
        if min_len > len(s):
            min_len = len(s)
            
    return min_len
