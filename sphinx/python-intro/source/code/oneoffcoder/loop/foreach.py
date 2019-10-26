# looping over an array/list
number_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in number_list:
    print(number)

# looping over a set
number_set = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

for number in number_set:
    print(number)

# looping over a tuple
number_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

for number in number_tuple:
    print(number)

# looping over a map
number_map = {
    'a': 0,
    'b': 1,
    'c': 2
}

for key, val in number_map.items():
    print(key, val)
