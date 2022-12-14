# We have two consecutive integers k1 and k2, k2 = k1 + 1
# We need to calculate the lowest strictly positive integer n, such that: the values nk1 and nk2 have the same digits but in different order.

# E.g.# 1:
# k1 = 100
# k2 = 101
# n = 8919
# Because 8919 * 100 = 891900 
# and     8919 * 101 = 900819

def find_lowest_int(k):
    k1, k2 = k, k + 1
    num = 0
    flag = False
    
    while flag != True:
        num += 1
        l1 = sorted([n for n in str(num * k1)])
        l2 = sorted([n for n in str(num * k2)])
        if l1 == l2:
            flag = True
    return num
