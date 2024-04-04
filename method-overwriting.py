#overwriting the parent class method

class Animal():

    def eat(self):
        print("This animal is eating!")


class Rabbit(Animal):

    def eat(self):
        print(f"This {self.__class__.__name__} is eating a carrot!")

rabbit = Rabbit()

rabbit.eat()
    