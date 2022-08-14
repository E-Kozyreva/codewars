# Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". 
# Input will always be valid, i.e. no negative integers.

def count_sheep(n):
    phrase = " sheep..."
    string = ""
    
    for sleep in range(n):
        string += str(sleep + 1) + phrase
    return string
