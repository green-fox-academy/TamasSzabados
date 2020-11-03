shop_items = ["Cupcake", 2, "Brownie", False]

# Accidentally we added "2" and "false" to the list.
# Your task is to change from "2" to "Croissant" and change from "false" to "Ice cream"
# No, don't just remove the items :)
# Create a function called sweets() which takes the list as a parameter.
# Expected output: "Cupcake", "Croissant", "Brownie", "Ice cream"
def sweets(shop_items):
    for i in range(len(shop_items)):
        if shop_items[i] == 2:
            shop_items[i] = "Croissant"
        if shop_items[i] == False:
            shop_items[i] = "Ice cream"
    return shop_items

print(sweets(shop_items))
