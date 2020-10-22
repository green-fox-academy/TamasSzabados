  
# Write a program that asks for a number.
# It would ask this many times to enter an integer,
# if all the integers are entered, it should print the sum and average of these
# integers like:
#
# Sum: 22, Average: 4.4

def parametric_average():
    times = int(input("Please enter how many numbers to calculate: "))
    num = []
    for i in range(times):
        num.append(float(input("Please enter a number: ")))

    Sum = sum(num)
    Avg = sum(num)/len(num)
    return print("Sum: "+ str(Sum) + ", " + "Average: " + str(Avg))

parametric_average()