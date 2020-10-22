# Write a program that reads a number from the standard input, then draws a
# square like this:
#
#
#
# %%%%%%
# %    %
# %    %
# %    %
# %    %
# %%%%%%
#
# The square should have as many lines as the number was


num1 = int(input("Please enter a number: "))

sign = "%"
space = " "
for i in range(0, num1):
    if i == 0 or i == num1-1:
        print(6*sign)
    else:
        print(sign + 4 * space + sign)