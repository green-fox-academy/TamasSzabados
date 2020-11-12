def bunnies(num):
    if num < 1:
        return num
    else:
        return 2 + bunnies(num-1)

print(bunnies(12))