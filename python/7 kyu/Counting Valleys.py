# You need count how many valleys you will pass. Start is always from zero level.
# Every time you go down below 0 level counts as an entry of a valley, and as you go up to 0 level from valley counts as an exit of a valley.
# One passed valley is equal one entry and one exit of a valley.
# s='FUFFDDFDUDFUFUF'
# U=UP
# F=FORWARD
# D=DOWN

def counting_valleys(s): 
    levels = {"U": 1, "F": 0, "D": -1, }
    level, count = 0, 0
    for val in range(len(s) - 1):
        level += levels[s[val]]
        if level < 0 and level + levels[s[val + 1]] == 0:
            count += 1
    return count
