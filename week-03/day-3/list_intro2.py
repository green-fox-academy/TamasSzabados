list_a = ["Apple", "Avocado", "Blueberries", "Durian", "Lychee"]

list_b = []
list_b.extend(list_a)

list_b.remove("Durian")

list_a.insert(4, "Kiwifruit")

print(list_a)

print("list a bigger" if list_a > list_b  else "list b bigger")

if "Durina" in list_b:
    print(list_b.index("Durian"))

list_b.extend(["Passion Fruit", "Pomelo"])
print(list_b)

print(list_a[2])

 