#inherit from the subclass
class Organism():
        Alive = True

class Animal(Organism):
    def eat(self):
        print("This animal is eating!")

class Dog(Animal):
     def bark(self):
          print("This dog barks!")

dog = Dog()

dog.eat()
print(dog.Alive)