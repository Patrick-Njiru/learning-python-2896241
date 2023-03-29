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
    def __init__(self, engine_type):
        super().__init__("Car")
        self.wheels = 4
        self.doors = 4
        self.engine_type = engine_type
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "car at", self.speed, "mph.") if self.speed > 0 else print("I have parked my car.")

class MotorCycle(Vehicle):
    def __init__(self, engine_type, has_side_car):
        super().__init__("MotorCycle")
        if(has_side_car):
            self.wheels = 3
        else:
            self.wheels = 2
        self.doors = 0
        self.engine_type = engine_type
    
    def drive(self, speed):
        super().drive(speed)
        print("Driving my", self.engine_type, "motorCycle at", self.speed, "mph.") if self.speed > 0 else print("I have parked my motorCycle.")

car1 = Car("gas")
car2 = Car("electric")
mc1 = MotorCycle("gas", True)
car1.drive(0)
car2.drive(60)
mc1.drive(100)

print(mc1)
print(car1)
print(car2)
