#
# Example file for working with classes
# LinkedIn Learning Python course by Joe Marini
#

class Vehicle():
    def __init__(self, bodystyle):
        self.bodystyle = bodystyle

    def drive(self, speed):
        self.mode = "driving"
        self.speed = speed

    def park(self, speed):
        self.mode = "parking"
        self.speed = speed

class Car(Vehicle):
    def __init__(self, enginetype):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "car at", self.speed, "mph.") if self.speed > 0 else print("I have parked my car.")

class Motorcycle(Vehicle):
    def __init__(self, enginetype, hassidecar):
        super().__init__("Motorcycle")
        if(hassidecar):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.enginetype = enginetype
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.enginetype, "motorcycle at", self.speed, "mph.") if self.speed > 0 else print("I have parked my motorcycle.")

car1 = Car("gas")
car2 = Car("electric")
mc1 = Motorcycle("gas", True)
car1.drive(0)
car2.drive(60)
mc1.drive(100)

print(mc1)
print(car1)
print(car2)
