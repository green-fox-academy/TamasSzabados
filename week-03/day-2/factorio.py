# - Create a function called `factorio`
#   that returns it's input's factorial

def factorio(num):
    factorial = 1
    for i in range(1,num):
        factorial *= i
    return factorial

x = int(input("Enter a number to calculate factorial: "))
print(factorio(x))

    