class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

    def get_year(self):
        return self.year

    def set_make(self, make):
        self.make = make

    def set_model(self, model):
        self.model = model

    def set_year(self, year):
        self.year = year


car = Car('Honda', 'Accord', 2019)

car.set_make('Toyota')
car.set_model('Supra')
car.set_year(2019)

print(f'{car.get_make()} {car.get_model()} {car.get_year()}')