def anagram(str1, str2):
    if type(str1) != str:
        raise TypeError("You must provide a string")
    
    elif type(str2) != str:
        raise TypeError("You must provide a string")

    elif sorted(str1) == sorted(str2):
        return True
    else:
        return False


print(anagram("abcd", "bdca"))