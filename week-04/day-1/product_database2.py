dict = {"Eggs" : 200,
"Milk" : 200,
"Fish" : 400,
"Apples" : 150,
"Bread"	: 50,
"Chicken": 550}

#Which products cost less than 201? (just the name)
cost_less =[]
for k,v in dict.items():
    if v<201:
        cost_less.append(k)
print("The following products cost less than 201:")
for i in cost_less:
    print("- " +i)
#Which products cost more than 150? (name + price)
cost_more ={}
for k,v in dict.items():
    if v>150:
        cost_more[k] = v
print("The following products cost more than 150:")
for k,v in cost_more.items():
    print("- " + k + " = " + str(v))