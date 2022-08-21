# Write a function that returns a string in which firstname is swapped with last name.
# Example(Input --> Output)
# "john McClane" --> "McClane john"

def name_shuffler(str_):
    return "{0} {1}".format(str_.split()[1], str_.split()[0])
