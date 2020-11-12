def strings(string1, x):
    new_string = ""
    if len(string1) < 1:
        return new_string
    elif string1[0] != x:
        new_string += string1[0]
    elif string1[0] == x:
        new_string += ""
    
    return new_string + strings(string1[1:],x)
        
print(strings("extra", "x"))