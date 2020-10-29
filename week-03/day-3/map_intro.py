dict = {}
print(len(dict))

dict = { 97 : "a", 98 : "b", 99 : "c", 65 : "A" , 66 :	"B", 67	:"C" }

print(dict.keys())
print(dict.values())

dict[68] = "D"


print(len(dict.items()))

print(dict[99])

del dict[97]

if 100 in dict.keys():
    print(dict[100])
else:
    print("no such key")

dict.clear()
print(dict)