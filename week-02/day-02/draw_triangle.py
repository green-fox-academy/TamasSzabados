# Write a program that reads a number from the standard input, then draws a
# triangle like this:
#
# *
# **
# ***
# ****
#
# The triangle should have as many lines as the number was

num1 = int(input("Please enter a number: "))
star = "*"
for i in range(0, num1+1):
    print(star*i)
    
