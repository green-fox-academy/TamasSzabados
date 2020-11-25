from fleet import Fleet
from thing import Thing

fleet = Fleet()

thing1 =Thing("Get milk")
thing2 =Thing("Remove the obstacles")
thing3 =Thing("Stand up")
thing4 =Thing("Eat lunch")

fleet.add(thing1)
fleet.add(thing2)
fleet.add(thing3)
fleet.add(thing4)

thing3.complete()
thing4.complete()





# - You have the `Thing` class
# - You have the `Fleet` class
# - You have the `fleet_of_things.py` file
# - Download those, use those
# - In the `fleet_of_things` file create a fleet
# - Achieve this output:
# Create a fleet of things to have this output:
# 1. [ ] Get milk
# 2. [ ] Remove the obstacles
# 3. [x] Stand up
# 4. [x] Eat lunch

print(fleet)
