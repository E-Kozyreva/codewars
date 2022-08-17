# Write a function to convert a name into initials. 
# This kata strictly takes two words with one space in between them.
# The output should be two capital letters with a dot separating them.

# It should look like this:
# Sam Harris => S.H
# patrick feeney => P.F

def abbrev_name(name):
    name, surname = name.split()[0], name.split()[1]
    initials = name[0].upper() + "." + surname[0].upper()
    return initials
