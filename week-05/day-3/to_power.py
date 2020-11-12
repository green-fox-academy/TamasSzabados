def to_power(num, power):
    if power == 1:
        return num
    else:
        return num * to_power(num,power - 1)

print(to_power(3,2))
        