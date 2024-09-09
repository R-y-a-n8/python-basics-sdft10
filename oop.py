class Car:

    def __init__(self, make, model, year):
        
        self.make = make
        self.model = model
        self.year = year

    def display_class(self):
        
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

my_car = Car(make="subaru", model="imprezza", year=2012)
my_car.display_class()