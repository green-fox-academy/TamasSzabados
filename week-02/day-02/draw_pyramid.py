# Write a program that reads a number from the standard input, then draws a
# pyramid like this:
#
#
#    *
#   ***
#  *****
# *******
#
# The pyramid should have as many lines as the number was

num1 = int(input("Please enter a number: "))*2
star = "*"
space = " "
for i in range(1, num1, 2):
    print(space * ((num1)//2-(i//2)) + star*i)