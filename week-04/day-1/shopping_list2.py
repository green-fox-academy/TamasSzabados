products = {"Milk":	1.07,
            "Rice":	1.59,
            "Eggs":	3.14,
            "Cheese": 12.60,
            "Chicken Breasts": 9.40,
            "Apples": 2.31,
            "Tomato": 2.58,
            "Potato": 1.75,
            "Onion": 1.10}

bob_list = {"Milk":	3,
            "Rice":	2,
            "Eggs":	2,
            "Cheese": 1,
            "Chicken Breasts": 4,
            "Apples": 1,
            "Tomato": 2,
            "Potato": 1}

alice_list= {"Rice": 1, 
            "Eggs": 5, 
            "Chicken Breasts": 2, 
            "Apples": 1, 
            "Tomato": 10}

#How much does Bob pay?
bob_spends = 0
for k,v in products.items():
    for j, i in bob_list.items():
        if k == j:
            bob_spends += v*i
print("Bob has to pay: " + str(bob_spends))


#How much does Alice pay?
alice_spends = 0
for k,v in products.items():
    for j, i in alice_list.items():
        if k == j:
            alice_spends += v*i
print("Alice has to pay: " + str(alice_spends))

#Who buys more Rice?
if alice_list["Rice"] > bob_list["Rice"]:
    print("Alice buys more Rice")
else:
    print("Bob buys more Rice")

#Who buys more Potato?
if "Potato" in alice_list.keys() and bob_list.keys():
    if alice_list["Potato"] > bob_list["Potato"]:
        print("Alice buys more Rice")
    else:
        print("Bob buys more Potato")
elif "Potato" not in alice_list.keys():
    if "Potato" in bob_list.keys():
        print("Bob buys more Potato")
elif "Potato" not in bob_list.keys():
    if "Potato" in alice_list.keys():
        print("Alice buys more Potato")
else:
    print("no one buys Potato")
#Who buys more different products?

if len(alice_list.values()) > len(bob_list.values()):
    print("Alice bought more different products")
elif len(alice_list.values()) == len(bob_list.values()):
    print("Same amount of different products")
else:
    print("Bob bought more different products")

#Who buys more products? 
if sum(alice_list.values()) > sum(bob_list.values()):
    print("Alice bought more products")
elif sum(alice_list.values()) == sum(bob_list.values()):
    print("Same amount of products")
else:
    print("Bob bought more products")