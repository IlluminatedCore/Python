class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def moves(self):
        print(f"This car moves along...")
    
    def get_make_model(self):
        print(f"This is a brand new {self.make}, model is {self.model}")

my_car = Vehicle('Hyundai', 'Tucson')

my_car.moves()
my_car.get_make_model()

print("**************")

class golfcart(Vehicle):
    pass

gc = golfcart('mini', "GC100")

gc.moves()
gc.get_make_model()

