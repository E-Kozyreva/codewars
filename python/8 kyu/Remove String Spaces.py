# Simple, remove the spaces from the string, then return the resultant string.

def no_space(str):
    return "".join([s for s in str if s != " "])
