def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False
    




def search_palindrome(str):
    output = []
    for i,k in enumerate(str):
        substr = ""
        for j, v in enumerate(str):
            if j > i + 2:
                substr = str[i:j]
                if palindrome(substr) == True:
                    output.append(substr)



    return output

print(search_palindrome("dog goat dad duck doodle never"))
