def strings(string1):
    new_string = ""
    if len(string1) < 1:
        return new_string
    elif len(string1) == 1:
        new_string += string1[0]
    else:
        new_string += string1[0] + "*"
    
    
    return new_string + strings(string1[1:])
        
print(strings("extra"))