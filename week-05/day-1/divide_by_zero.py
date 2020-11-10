# Create a function that takes a number,
# divides ten with it,
# and prints the result.
# It should print "fail" if the parameter is 0

def divider(num):
    try:
        divide = 10/num
        print(divide)
    except ZeroDivisionError:
        print("Fail")

number = int(input("Please enter a number: "))
divider(number)