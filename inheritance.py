#inherit from the parent class

class Animal():
    Alive = True

    def eat(self):
        print("This animal is eating!")
    
    def sleep(self):
        print("This animal is sleeping 😴")

class Rabbit(Animal):
    pass


rabbit = Rabbit() # this is called object

rabbit.eat()
