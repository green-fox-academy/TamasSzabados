def strings(string1, x, y):
    new_string = ""
    if len(string1) < 1:
        return new_string
    elif string1[0] != x:
        new_string += string1[0]
    elif string1[0] == x:
        new_string += y
    
    return new_string + strings(string1[1:],x,y)
        
print(strings("otto", "t", "l"))