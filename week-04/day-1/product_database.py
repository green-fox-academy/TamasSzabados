dict ={"Eggs" : 200, "Milk" : 200, "Fish" : 400, "Apples": 150, "Bread": 50, "Chicken" : 550}

#How much is the fish?

print("The fish is: " + str(dict["Fish"]))
#What is the most expensive product?
max_price = 0
most_expensive = ""
for k, v in dict.items():
    if v > max_price:
        max_price = v
        most_expensive = k
print("Most expensive product: " + str(most_expensive))



#What is the average price?
print("The average price is: " + str(round(sum(dict.values())/len(dict.values()),2)))

#How many products' price is below 300?
num = 0
for v in dict.values():
    if v < 300:
        num += 1
print("The number of products below 300 is: " + str(num))


#Is there anything we can buy for exactly 125?
exactly = []
for k, v in dict.items():
    if v == 125:
        exactly.append(k)

if len(exactly) > 0:
    print("You can buy for exactly 125 the following products" + str(exactly))
else:
    print("No such products found")
    

#What is the cheapest product?
v=list(dict.values())
k=list(dict.keys())
print("The cheapest product is: " + str(k[v.index(min(v))]))