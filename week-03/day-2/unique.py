#  Create a function that takes a list of numbers as a parameter
#  Returns a list of numbers where every number in the list occurs only once

def unique(arr):
    list1 = set(arr)
    list2 = list(list1)
    return list2
    
#  Example
print(unique([1, 11, 34, 11, 52, 61, 1, 34]))
#  should print: `[1, 11, 34, 52, 61]`