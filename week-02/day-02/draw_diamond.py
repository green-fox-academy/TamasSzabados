# Write a program that reads a number from the standard input, then draws a
# diamond like this:
#
#
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
#
# The diamond should have as many lines as the number was


num1 = int(input("Please enter a number: "))

star = "*"
space = " "
for i in range(1, num1, 2):
    print(space * ((num1)//2-(i//2)) + star*i)
for i in range(1, num1, 2):
    print(space * ((i//2)+1) + star*((num1)-(i)))