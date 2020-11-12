def bunnies(num):
    if num < 1:
        return num
    elif num %2 == 0:
        return 2 + bunnies(num-1)
    else:
        return 3 + bunnies(num-1)

print(bunnies(12))