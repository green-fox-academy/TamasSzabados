from pirate import Pirate
from ship import Ship
from armada import Armada


def main():
    santa_maria = Ship()
    broken_bones = Ship()
    sea_dog = Ship()
    one_eye = Ship()
    
    santa_maria.fill_ship()
    broken_bones.fill_ship()
    sea_dog.fill_ship()
    one_eye.fill_ship()
    print(santa_maria)
    print(broken_bones)
    santa_maria.battle(broken_bones)
    armada1 = Armada()
    armada2 = Armada()

    armada1.add_ship(santa_maria)
    armada1.add_ship(broken_bones)
    armada2.add_ship(sea_dog)
    armada2.add_ship(one_eye)
    armada1.armada_war(armada2)


if __name__ == "__main__":
    main()