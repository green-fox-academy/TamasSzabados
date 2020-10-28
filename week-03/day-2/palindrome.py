def create_palindrome(str):

    palindrome = str + str[::-1]
    return palindrome

print(create_palindrome("greenfox"))