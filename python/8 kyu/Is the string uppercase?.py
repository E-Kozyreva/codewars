def is_uppercase(inp):
    
    flag = True
    
    for symbol in inp:
        if symbol != symbol.upper():
            flag = False
    
    return flag
