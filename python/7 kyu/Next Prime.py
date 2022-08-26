# Get the next prime number!
# You will get a numbern (>= 0) and your task is to find the next prime number.
# Make sure to optimize your code: there will numbers tested up to about 10^12.

# Examples
# 5   =>  7
# 12  =>  13

def isprime(num):
    for p in range(2, int(num**0.5) + 1):
        if num % p == 0:
            return False
    return True


def next_prime(n):
    if n == 0:
        return 2
    else:
        n += 1
        while isprime(n) != True:
            n += 1
        return n
