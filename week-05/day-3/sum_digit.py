def sum_number(digit):
    sum = 0
    if digit <=10:
        return digit
    else:
        sum += digit%10
        return sum + sum_number(digit//10)

print(sum_number(1262))