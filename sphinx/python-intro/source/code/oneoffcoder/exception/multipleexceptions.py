def get_best_car(make, model):
    makes = {
        'honda': ['accord', 'civic', 'crv'],
        'toyota': ['camry', 'avalon', 'sienna']
    };

    return makes[make.lower()][model]


# valid
print(get_best_car('Honda', 1))

# throws IndexError
print(get_best_car('Honda', 4))

# throws KeyError
print(get_best_car('Ford', 1))

# catch multiple exceptions
try:
    print(get_best_car('Ford', 3))
except IndexError:
    print('invalid model')
except KeyError:
    print('invalid make')
