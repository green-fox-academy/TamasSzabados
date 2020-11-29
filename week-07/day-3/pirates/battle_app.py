from pirate import Pirate
from ship import Ship

pirate1 = Pirate("Dreadful")
pirate2 = Pirate("Blackbeard")
pirate3 = Pirate("Jassy")
pirate4 = Pirate("Black Jack")
pirate5 = Pirate("Seadog")
pirate6 = Pirate("James")
pirate7 = Pirate("Dude")
pirate8 = Pirate("Half Blind")

pirate5.drinkSomeRum()
pirate6.drinkSomeRum()
pirate8.drinkSomeRum()


santa_maria = Ship("santa maria")
bone_heart = Ship("bone heart")

santa_maria.fillShip(pirate1, [pirate2,pirate3,pirate4])
bone_heart.fillShip(pirate5, [pirate6,pirate7,pirate8])

santa_maria.battle(bone_heart)


