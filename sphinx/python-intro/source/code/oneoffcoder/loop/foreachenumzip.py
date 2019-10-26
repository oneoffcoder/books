names = ['Jack', 'John', 'Joe']
ages = [18, 19, 20]

for i, (name, age) in enumerate(zip(names, ages)):
    print(i, name, age)
