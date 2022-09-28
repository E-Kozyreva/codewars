# Define a function that removes duplicates from an array of numbers and returns it as a result.
# The order of the sequence has to stay the same.

def distinct(seq):
    new_seq = []
    for num in seq:
        if num not in new_seq:
            new_seq.append(num)
    return new_seq
