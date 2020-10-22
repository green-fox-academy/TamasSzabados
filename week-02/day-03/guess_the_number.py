# Write a program that stores a number, and the user has to figure it out.
# The user can input guesses, after each guess the program would tell one
# of the following:
#
# The stored number is higher
# The stried number is lower
# You found the number: 8

num1 = int(input("Please enter a number: "))
num2= 36
found = False

while found == False:
    if num1<num2:
        print("The stored number is higher")
        num1 = int(input("Please enter a number: "))
          
            
    elif num1>num2:
        print("The stried number is lower")
        num1 = int(input("Please enter a number: "))      
    else:
        print("You found the number: " + str(num1)) 
        found = True 


