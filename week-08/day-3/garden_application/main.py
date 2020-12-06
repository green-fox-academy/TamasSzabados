from garden import Garden, Flowers, Trees

def main():
    garden = Garden()
    flower1 = Flowers("yellow")
    flower2 = Flowers("blue")
    tree1 = Trees("purple")
    tree2 = Trees("orange")

    garden.add(flower1)
    garden.add(flower2)
    garden.add(tree1)
    garden.add(tree2)

    garden.describe_garden()
    garden.watering(40)
    garden.watering(70)

if __name__ == '__main__':
    main()





