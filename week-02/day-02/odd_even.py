 
# Write a program that reads a number from the standard input,
# Then prints "Odd" if the number is odd, or "Even" if it is even.
print("Please input a number: ")
num = int(input())

if num % 2 == 0:
    print("Even")
else:
    print("Odd")