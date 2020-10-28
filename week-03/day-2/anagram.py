def anagram(str1, str2):
    res1 = ''.join(sorted(str1))
    res2 = ''.join(sorted(str2))
    if res1 == res2:
        return True
    else:
        return False


print(anagram("green", "fox"))
print(anagram("dog", "god"))
