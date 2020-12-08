from aircraft_carrier import Aircrafts, F16, F35, Carrier


def main():
    tomcat = F16()
    raptor = F16()
    falcon = F16()
    desert_fox = F16()
    double_barrel = F35()
    panther = F35()
    lightning = F35()
    tornado = F35()
    typhoon = F35()

    typhoon.get_type()
    typhoon.refill(20)
    typhoon.fight()
    typhoon.refill(20)
    print(typhoon.refill(20))
    typhoon.get_status()
    print(typhoon.is_priority())

    nimitz = Carrier(1000,500)

    nimitz.add(tomcat)
    nimitz.add(raptor)
    nimitz.add(falcon)
    nimitz.add(panther)
    nimitz.add(lightning)
    nimitz.add(typhoon)
    nimitz.get_status()
    nimitz.fill()
    nimitz.get_status()

    enterprise = Carrier(500,100)

    enterprise.add(tomcat)
    enterprise.add(raptor)
    enterprise.add(falcon)
    enterprise.add(panther)
    enterprise.add(lightning)
    enterprise.add(typhoon)
    enterprise.get_status()
    enterprise.fill()
    enterprise.get_status()

    enterprise.fight(nimitz)
    enterprise.get_status()
    nimitz.get_status()




if __name__ == "__main__":
    main()