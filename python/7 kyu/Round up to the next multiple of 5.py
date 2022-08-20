# Given an integer as input, can you round it to the next (meaning, "greater than or equal") multiple of 5?
# Examples:
# input:    output:
# 0    ->   0
# 2    ->   5
# 30   ->   30
# -2   ->   0
# -5   ->   -5
# etc.

def round_to_next5(n):
    if n % 5 == 0:
        return n
    else:
        while n % 5 != 0:
            n += 1
        return n
