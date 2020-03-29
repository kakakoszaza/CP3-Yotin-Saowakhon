class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def TurnOnAir(self):
        print("Turn On : Air\n")

class Car(Vehicle):
    pass

class Pickup(Vehicle):
    pass

class Van(Vehicle):
    pass

class Estatecar(Vehicle):
    pass

car1 = Car()
car1.TurnOnAir()

Pickup1 = Pickup()
Pickup1.TurnOnAir()

Van1 = Van()
Van1.TurnOnAir()

estatecar1 = Estatecar()
estatecar1.TurnOnAir()