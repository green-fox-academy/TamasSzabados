from car import Car
from station import Station

opel = Car()
mol = Station()

print(opel.gas_amount)
mol.refill(opel)
print(opel.gas_amount)
print(mol.gas_amount)
