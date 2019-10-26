class Car(object):
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def __repr__(self):
        return f"{{'make': {self.make}, 'model': {self.model}, 'year': {self.year}}}"

    def __str__(self):
        return f'Car(make={self.make}, model={self.model}, year={self.year})'


car = Car('Honda', 'Accord', 2019)

print(car)
print(repr(car))
