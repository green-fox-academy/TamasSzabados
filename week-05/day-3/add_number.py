def add_number(number):
    if number <= 1:
        return number
    else:
        return number + add_number(number - 1)

print(add_number(4))
        
      