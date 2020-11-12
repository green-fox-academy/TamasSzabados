def max_finder(args):
    if len(args) == 1:
        return args[0]
    else:
        return max(args[0],max_finder(args[1:]))



list1 = [1, 4, 3, 6, 7, 1]

print(max_finder(list1))

