names = []
print(len(names))
names.append("William")

if len(names) == 0:
   print("List is empty")
else:
    print("List contains: " + str(len(names)) + " element(s)")

names.extend(["John", "Amanda"])
print("List contains: " + str(len(names)) + " element(s)")

print(names[-1])


for i in names:
    print(str(i))

for i, k in enumerate(names, 1):
    print(str(i) + ".   " + k)

names.remove(names[1])   

for i in names[::-1]:
    print(i)

del names[:]
