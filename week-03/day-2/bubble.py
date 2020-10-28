#  Create a function that takes a list of numbers as parameter
#  Returns a list where the elements are sorted in ascending numerical order
#  Make a second boolean parameter, if it's `True` sort that list descending


def bubble(arr):
    arr.sort()
    return arr


def advanced_bubble(arr, is_descending=True):
    arr.sort(reverse=is_descending)
    return arr


#  Example:
print(bubble([43, 12, 24, 9, 5]))
#  should print [5, 9, 12, 24, 34]
print(advanced_bubble([43, 12, 24, 9, 5], True))
#  should print [34, 24, 9, 5]