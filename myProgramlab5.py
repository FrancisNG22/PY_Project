class Vehicle:
    def __init__(self, number_of_wheels, type_of_tanks, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.type_of_tanks = type_of_tanks
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

    def drive(self):
        if (self.number_of_wheels == '4'):
            print("The vehicle is on driving mode now.")
        else:
            print("The vehicle is not on driving mode now.")
            

class ElectricCar(Vehicle):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Vehicle.__init__(self, number_of_wheels, 'electric', seating_capacity, maximum_velocity)


vios = Vehicle('4','petrol',5,180)
bmw = Vehicle('6','diesel',10,120)


print("VIOS number of wheels = " + vios.number_of_wheels)
print("BMW number of wheels = " + bmw.number_of_wheels)

print("VIOS type of tank = " + vios.type_of_tanks)
print("BMW type of tank = " + bmw.type_of_tanks)

print("VIOS seating capacity = " + str(vios.seating_capacity))
print("BMW seating capacity = " + str(bmw.seating_capacity))

print("VIOS maximum velocity = " + str(vios.maximum_velocity))
print("BMW maximum velocity = " + str(bmw.maximum_velocity))

vios.drive()
bmw.drive()

blueSG = ElectricCar('4', 5, 150)
print("BlueSG type of tank = " + blueSG.type_of_tanks)
blueSG.drive()
