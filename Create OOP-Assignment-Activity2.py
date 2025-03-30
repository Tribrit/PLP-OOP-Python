
# Vehicle class and polymorphism example 

class Vehicle:
    def move(self):
        """All vehiles move but in diffrent ways"""  # Typos: "vehiles" should be "vehicles", "diffrent" should be "different"
        pass  

# Car class  
class Car(Vehicle):
    def move(self):
        """A car moves by driving on roads"""
        print("Driving ")  

# Plane class  
class Plane(Vehicle):
    def move(self):
        """A plane moves by flying in the sky"""
        print("Flying ✈")  

# Boat class  
class Boat(Vehicle):
    def move(self):
        """A boat moves by sailing on water"""
        print("Sailing ")  

# Using the classes  
vehicles = [Car(), Plane(), Boat()]  

for v in vehicles:
    v.move()  # Calls each move method depending on the object type  
