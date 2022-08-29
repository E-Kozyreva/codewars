# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:
# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.
# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    values = {"i": 1, "d": -1, }
    num, answer = 0, []
    for val in data:
        if val == "i" or val == "d":
            num += values[val]
        elif val == "s":
            num  = num ** 2
        elif val == "o":
            answer.append(num)
        else:
            num += 0
    return answer
