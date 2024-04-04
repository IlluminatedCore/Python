#prevents a user from creating an object of that class.

#abstract class = a class which contains one or more abstract methods
#abstract method = a method that has declaration but has no implementation.

from abc import ABC, abstractmethod

class Vehicle(ABC):

    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop():
        pass

class Car(Vehicle):

    def go(self):
        print("This car is driving")
    
    def stop():
        print("This car is stopped")

vehicle = Vehicle() # this wont work because abstract method is used in that class

maruti = Car()


print(maruti.go())
print(vehicle.go()) 




