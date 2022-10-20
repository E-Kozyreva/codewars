# Your Task:
# Given the duration of the planet's orbit (in days) and a specific year on this planet, determine if the given year is a leap year here.

# For example:
# On Earth, a single rotation around the sun takes 365.25 days. Therefore, each year takes 365 days but every forth year is a leap year and takes 366 days. 
# The next leap year on Earth will occur in 2020.

def is_leap_year(d, y):
    return True if int(d * y) == d * y else False
