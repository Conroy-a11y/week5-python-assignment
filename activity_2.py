# Base class (general concept of "Mover")
class Mover:
    def move(self):
        pass  # This will be overridden by child classes


# Vehicle classes
class Car(Mover):
    def move(self):
        print("Driving 🚗")

class Plane(Mover):
    def move(self):
        print("Flying ✈️")


# Animal classes
class Dog(Mover):
    def move(self):
        print("Running 🐕")

class Fish(Mover):
    def move(self):
        print("Swimming 🐟")


# Demonstration
objects = [Car(), Plane(), Dog(), Fish()]

for obj in objects:
    obj.move()
