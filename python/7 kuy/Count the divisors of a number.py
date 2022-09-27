# Count the number of divisors of a positive integer n.

def divisors(n):
    count = 0
    for div in range(1, n + 1):
        if n % div == 0:
            count += 1
    return count
