dict = {"978-1-60309-452-8" : "A Letter to Jo", "978-1-60309-459-7" :	"Lupus", "978-1-60309-444-3"  : "Red Panda and Moon Bear", 
"978-1-60309-461-0" : "The Lab"}

for k, v in dict.items():
    print(v + " (ISBN: "+ k + ")")

del dict["978-1-60309-444-3"]

for k, v in dict.items():
    if v == "The Lab":
        keytodel = k
        
del dict[keytodel]

dict["978-1-60309-450-4"] = "They Called Us Enemy"
dict["978-1-60309-453-5"] = "Why Did We Trust Him?"

print("yes there is a key" if "478-0-61159-424-8" in dict.keys() else " no such key")

print(dict["978-1-60309-453-5"])