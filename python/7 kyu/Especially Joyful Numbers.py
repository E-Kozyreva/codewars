# We are interested in Harshad numbers where the product of its digit sum s and s with the digits reversed, gives the original number n. For example consider number 1729:
# its digit sum, s = 1 + 7 + 2 + 9 = 19
# reversing s = 91
# and 19 * 91 = 1729 --> the number that we started with.

def number_joy(n):
    sum_n = sum([int(num) for num in str(n)])
    product = sum_n * int(str(sum_n)[::-1])
    return product == n
