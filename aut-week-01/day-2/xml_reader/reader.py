from lxml import etree

with open("food.xml", "r") as f:
    tree = etree.parse(f)

    #The price of all foods (as a list)
    elements_price = tree.xpath('/breakfast_menu/food/price/text()')
    print(elements_price)

    #The sum of all the calories
    elements_calories = tree.xpath('sum(/breakfast_menu/foods/calories/text())')
    print(elements_calories)

    #The description of the food with the id: 3
    element_description = tree.xpath('/breakfast_menu/food[@id="3"]/description/text()')
    print(element_description)

    #The price of "French Toast"
    french_toast_price = tree.xpath('/breakfast_menu/food[name ="French Toast"]/price/text()')
    print(french_toast_price)

    #The concatenated descriptions of all the "savoury" foods
    savoury_desc = tree.xpath('/breakfast_menu/food[@type="savoury"]/description/text()')
    print(savoury_desc)

    #The count of ingredients of the food with id: 2
    ingredients_2 = tree.xpath('count(//food[@id="2"]/ingredients/ingredient)')
    print(ingredients_2)

    #The second ingredient of "Homestyle Breakfast"
    homestyle = tree.xpath('/breakfast_menu/food[name="Homestyle Breakfast"]/ingredients/ingredient/type/text()')
    print(homestyle[1])

    #The count of foods that has "milk" in the ingredients
    milk_ingr = tree.xpath('count(/breakfast_menu/food/ingredients/ingredient[type="milk"]/type/text())')
    print(milk_ingr)

    #The count of ingredients of all "sweet" foods
    sweet_count = tree.xpath('count(/breakfast_menu/food[@type="sweet"]/ingredients/ingredient/type/text())')
    print(sweet_count)








