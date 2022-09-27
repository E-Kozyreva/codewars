# Your task is to write a function which returns the sum of following series upto nth term(parameter).
# Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...

def series_sum(n):
    div = 1
    sum_of_numbers = 0
    for count in range(n):
        sum_of_numbers += 1/div
        div += 3
    return format(sum_of_numbers, '.2f')
