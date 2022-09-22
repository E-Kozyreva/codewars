# You have to write a calculator that receives strings for input. The dots will represent the number in the equation. 
# There will be dots on one side, an operator, and dots again after the operator. The dots and the operator will be separated by one space.
# Here are the following valid operators :

# + Addition
# - Subtraction
# * Multiplication
# // Integer Division

def calculator(txt):
    data = txt.split(" ")
    len_d0, len_d2 = len(data[0]), len(data[2])
    if data[1] == "+":
        return data[0][0] * (len_d0 + len_d2)
    elif data[1] == "-":
        return data[0][0] * (len_d0 - len_d2)
    elif data[1] == "*":
        return data[0][0] * (len_d0 * len_d2)
    else:
        return data[0][0] * (len_d0 // len_d2)
