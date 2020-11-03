list1 = [500, 1000, 1250, 175, 800, 120]


print("You have spent: " + str(sum(list1)))
print("The greatest expense was: " + str(max(list1)))
print("The cheapest spending was: " + str(min(list1)))
print("The average amount spent was: " + str(round(sum(list1)/len(list1),2)))

sum_spent = 0
for i in list1:
    sum_spent += i
print(sum_spent)

max_spent = 0
for i in list1:
    if i > max_spent:
        max_spent = i
print(max_spent)

min_spent = list1[0]
for i in list1:
    if i < min_spent:
        min_spent = i
print(min_spent)

print(sum_spent/len(list1))