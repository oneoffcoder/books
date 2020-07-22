from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_noise(self):
        pass

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f'{self.name} says woof')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name)

    def make_noise(self):
        print(f'{self.name} says meow')

animals = [Dog('clifford'), Cat('heathcliff')]
for animal in animals:
    animal.make_noise()