class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year


car = Car('Honda', 'Accord', 2019)

print(f'{car.make} {car.model} {car.year}')
